#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <shlobj.h>
#include <windows.h>
#include <sys/types.h>
#include <sys/stat.h>


std::string appdata;
std::string folderPath;
    

int createDirectories(){
    std::filesystem::create_directories(folderPath);
    std::filesystem::create_directories(folderPath + "\\game");
    std::filesystem::create_directories(folderPath + "\\path");


    std::ofstream outfile (folderPath + "\\unzipPath.txt");
    outfile.close();

    return 0;
}


int main() {

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



    std::cout << "\n\n\n\nthe folderpath specified is : " << folderPath;

    

    return 0;
}
