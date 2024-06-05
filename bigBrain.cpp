#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <sys/types.h>
#include <sys/stat.h>
#include <vector>
#include "C:\Users\Pekmi\Documents\.UnitProject\working games!\Assets\theRealPart\include\miniz.h"


std::string appdata;
std::string folderPath;
std::string zipFilePath; // = "path/to/your.zip";
std::string outputDir; //= "path/to/output/dir";
    

int createDirectories(){
    std::filesystem::create_directories(folderPath);
    std::filesystem::create_directories(folderPath + "\\game");
    std::filesystem::create_directories(folderPath + "\\path");
    std::filesystem::create_directories(folderPath + "\\download");
    std::filesystem::create_directories(folderPath + "\\unzipped");


    std::ofstream outfile (folderPath + "\\unzipPath.txt");
    outfile.close();

    return 0;
}

int checkExistingDirectories(){
    appdata = getenv("APPDATA");
    folderPath = (appdata + "\\workingGames");
    struct stat info;
    //check if the directory exists
    if( stat( folderPath.c_str(), &info ) != 0 )
        //can't access
        printf( "cannot access %s\n", folderPath.c_str() );
    else if( info.st_mode & S_IFDIR ) 
        //exist
        printf( "%s is a directory\n", folderPath.c_str() );
    else
        //doesnt exist
        printf( "%s is no directory\n", folderPath.c_str() );
        createDirectories();    

    return 0;
}

bool unzipFile(const std::string& zipFolderPath, const std::string& outputDir) {
    for (const auto& entry : std::filesystem::directory_iterator(zipFolderPath)) {
        // Check if the entry is a regular file
        if (entry.is_regular_file()) {
            std::string zipFilePath = entry.path().string();
            
            mz_zip_archive zip_archive;
            memset(&zip_archive, 0, sizeof(zip_archive));

            if (!mz_zip_reader_init_file(&zip_archive, zipFilePath.c_str(), 0)) {
                std::cerr << "Failed to open zip file: " << zipFilePath << std::endl;
                return false;
            }

            int fileCount = mz_zip_reader_get_num_files(&zip_archive);
            if (fileCount == 0) {
                std::cerr << "No files found in the zip file: " << zipFilePath << std::endl;
                mz_zip_reader_end(&zip_archive);
                return false;
            }

            // Assuming you want to extract to the provided output directory
            std::string outputPath = outputDir;

            for (int i = 0; i < fileCount; ++i) {
                mz_zip_archive_file_stat file_stat;
                if (!mz_zip_reader_file_stat(&zip_archive, i, &file_stat)) {
                    std::cerr << "Failed to get file info for file index " << i << std::endl;
                    mz_zip_reader_end(&zip_archive);
                    return false;
                }

                std::vector<char> fileData(file_stat.m_uncomp_size);

                if (!mz_zip_reader_extract_to_mem(&zip_archive, i, fileData.data(), fileData.size(), 0)) {
                    std::cerr << "Failed to extract file: " << file_stat.m_filename << std::endl;
                    mz_zip_reader_end(&zip_archive);
                    return false;
                }

                // Append the filename to the output directory
                outputPath = outputPath + "/" + file_stat.m_filename;

                // Create the directories if necessary
                std::filesystem::create_directories(std::filesystem::path(outputPath).parent_path());

                // Write the extracted data to the output file
                std::ofstream outputFile(outputPath, std::ios::binary);
                outputFile.write(fileData.data(), fileData.size());
                outputFile.close();
            }

            // Close the ZIP archive
            mz_zip_reader_end(&zip_archive);

            std::cout << "Unzip successful!" << std::endl;
            return true;
        }
    }

    std::cerr << "No zip files found in the provided folder: " << zipFolderPath << std::endl;
    return false;
}



int main() {
    checkExistingDirectories();    

    
    zipFilePath = (folderPath + "\\download");
    outputDir = (folderPath + "\\unzipped");

    if (unzipFile(zipFilePath, outputDir)) {
        std::cout << "Unzipped successfully!" << std::endl;
    } else {
        std::cerr << "Unzip failed!" << std::endl;
    }
}
