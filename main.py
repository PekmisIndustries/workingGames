import os
import os.path
import sys
import time


def create_directories():
    os.makedirs("wg\\game", exist_ok=True)
    os.makedirs("wg\\path", exist_ok=True)
    os.makedirs("wg\\download", exist_ok=True)
    os.makedirs("wg\\unzipped", exist_ok=True)
    return 0

def get_skrakmi_file():
    while True:
        sfile = input("Provide a Skrakmi file: ")
        sfile = sfile.strip("'")
        sfile = sfile.strip('"')
        if sfile.startswith("& "):
            sfile = sfile[2:]
        try:
            with open(sfile, "r") as f:
                output = [f.readline().strip() for _ in range(6)]
                return output
        except FileNotFoundError:
            print("File not found. Please try again.")
        except Exception as e:
            print(f"Error reading file: {e}")


def create_game_folder(game_name):
    os.makedirs(game_name, exist_ok=True)
    return 0

def download_game_torrent(magnet_link):
    aria_path = os.path.abspath("aria/aria2c.exe")
    save_path = os.path.abspath("wg\\download")
    with open("ariaPath.txt", "w") as f:
        f.write(aria_path) 
    with open("magnetToDownload.txt", "w") as m:
        m.write(magnet_link)
    with open("downloadFolderPath.txt", "w") as m:
        m.write(save_path)
    os.startfile("magnet.sh")



create_directories()

sf = get_skrakmi_file()
create_game_folder(sf[0])

if(sf[1] == "1"):
    download_game_torrent(sf[3])
    pass
if(sf[1] == "0"):
    #download_game_link(sf[2])
    pass




#os.startfile("unzipper.py")