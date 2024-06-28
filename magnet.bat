@echo off
setlocal

rem Set the directory of the current script
set WG_FOLDER=%~dp0wg

rem Read paths and URLs from the text files
set /p ARIA2C_EXE_PATH=<"%WG_FOLDER%\ariaPath.txt"
set /p MAGNET_URL=<"%WG_FOLDER%\magnetToDownload.txt"
set /p DOWNLOAD_FOLDER=<"%WG_FOLDER%\downloadFolderPath.txt"

rem Convert Unix-style paths to Windows-style paths if needed
for %%F in ("%DOWNLOAD_FOLDER%") do set "DOWNLOAD_FOLDER_WINDOWS=%%~fF"

rem Ensure the path conversion is correct
if not defined DOWNLOAD_FOLDER_WINDOWS (
    echo Error: Unable to convert the download folder path.
    pause
    exit /b 1
)

rem Display the magnet URL and start downloading
echo Downloading: "%MAGNET_URL%"
echo Running command: "%ARIA2C_EXE_PATH%" --dir="%DOWNLOAD_FOLDER_WINDOWS%" --seed-time=0 --file-allocation=none "%MAGNET_URL%"
"%ARIA2C_EXE_PATH%" --dir="%DOWNLOAD_FOLDER_WINDOWS%" --seed-time=0 --file-allocation=none -V --disable-ipv6 "%MAGNET_URL%"

rem Check the result of the download operation
if %errorlevel% neq 0 (
    echo Error: aria2c encountered a problem.
    pause
    exit /b 1
)

rem Write download complete indicator
echo Download complete! > "%WG_FOLDER%\download_complete.txt"