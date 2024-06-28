import os
import os.path
import time
import shutil
import subprocess

def open_file(filename):
    if sys.platform == "win32":
        os.startfile("magnet.bat")
    else:
        os.system("exo-open --launch TerminalEmulator ./magnet.sh")


def reset():
    if os.path.isfile("wg"):
        os.rmdir("wg", ignore_errors=True)
    print("reset done")

def create_directories():
    os.makedirs("wg/game", exist_ok=True)
    os.makedirs("wg/path", exist_ok=True)
    os.makedirs("wg/download", exist_ok=True)
    os.makedirs("wg/unzipped", exist_ok=True)
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
                output = [f.readline().strip() for _ in range(10)]
                return output
        except FileNotFoundError:
            print("File not found. Please try again.")
        except Exception as e:
            print(f"Error reading file: {e}")

def create_game_folder(game_name):
    os.makedirs(os.path.join("wg", game_name), exist_ok=True)
    return 0

def download_game_torrent(magnet_link):
    aria_path = "dependancies/aria2c.exe"
    save_path = os.path.abspath("wg/download")
    with open("wg/ariaPath.txt", "w") as f:
        f.write(aria_path) 
    with open("wg/magnetToDownload.txt", "w") as m:
        m.write(magnet_link)
    with open("wg/downloadFolderPath.txt", "w") as n:
        n.write(save_path)
    print("Created paths text files")
    print("Starting download process")
    #os.startfile("magnet.sh")
    #os.startfile("magnet.py")
    open_file

def move_downloaded_game():
    for filename in os.listdir("wg/download"):
        file_path = os.path.join("wg/download", filename)
        shutil.move(file_path, "wg/unzipped")

def check_download_state():
    while True:
        time.sleep(2)
        if(os.path.exists("wg/download_complete.txt")):
            os.remove("wg/download_complete.txt")
            return 0
        
def check_unzipping_state():
    while True:
        time.sleep(2)
        if(os.path.exists("wg/unzipped.txt")):
            os.remove("wg/unzipped.txt")
            return 0

def apply_crack(crack_path, crack_destination):
    for filename in os.listdir(crack_path):
        file_path = os.path.join(crack_path, filename)
        dest_path = os.path.join(crack_destination, filename)
        if os.path.exists(dest_path):
            os.remove(dest_path)
        shutil.move(file_path, crack_destination)
    print("crack applied")

def move_game_to_personal_folder():
    origin = os.path.abspath("wg/unzipped")
    destination = os.path.join("wg/", sf[0])
    for filename in os.listdir(origin):
        file_path = os.path.join(origin, filename)
        shutil.move(file_path, destination)


#----------------------------------------------------------


reset()
create_directories()
print("Verified directories")

sf = get_skrakmi_file()
print("Found Skrakmi file")

create_game_folder(sf[0])
print("Created game directory")

if(sf[1] == "1"):
    print("Torrent/Magnet detected\nDownloading game")
    download_game_torrent(sf[3])
if(sf[1] == "0"):
    #download_game_link(sf[2])
    pass

check_download_state()

if(sf[4] == "1"):
    print("download zipped\nunzipping download")
    os.startfile("unzipper.py")
    check_unzipping_state()
if(sf[4] == "0"):
    print("download already unzipped\nmoving download")
    move_downloaded_game()

if(sf[5] == "1"):
    print("applying crack")
    apply_crack(os.path.join("wg/unzipped/", sf[6]), os.path.join("wg/unzipped/", sf[7]))

print("moving game")
move_game_to_personal_folder()

input("Game Ready!\nType something to launch the game!")
os.startfile(os.path.join("wg/", sf[0], sf[8]))