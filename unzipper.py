import zipfile
import os
from pathlib import Path

def delete_download_file(path):
    print("removing file")
    os.remove(path)

def find_single_zip_file(directory):
    zip_files = list(Path(directory).glob('*.zip'))
    if len(zip_files) == 1:
        return zip_files[0]
    elif len(zip_files) == 0:
        print(f"Error: No zip files found in {directory}.")
    else:
        print(f"Error: Multiple zip files found in {directory}.")
    return None

def unzip_file(zip_path, extract_to):
    os.makedirs(extract_to, exist_ok=True)
    print("unzipping, please wait :)")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Unzipped {zip_path} to {extract_to}")

    delete_download_file(zip_path)
    

download_folder = "wg/download"
zip_file_path = find_single_zip_file(download_folder)
destination_folder = "wg/unzipped"

unzip_file(zip_file_path, destination_folder)

with open("wg/unzipped.txt", 'w') as f:
    f.write("unzipped :3")

print("ended successfully")