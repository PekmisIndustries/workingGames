@echo off
setlocal
rem Set variables
set WG_FOLDER=%~dp0wg
set /p ARIA2C_EXE_PATH=<"%WG_FOLDER%\ariaPath.txt"
set /p MAGNET_URL=<"%WG_FOLDER%\magnetToDownload.txt"
set DOWNLOAD_FOLDER=%WG_FOLDER%\download

rem Convert DOWNLOAD_FOLDER path if needed
set DOWNLOAD_FOLDER_WINDOWS=%DOWNLOAD_FOLDER%

rem Run aria2c
"%ARIA2C_EXE_PATH%" --seed-time -d "%MAGNET_URL%" --dir "%DOWNLOAD_FOLDER_WINDOWS%"

rem Write download complete indicator
echo Download complete! > "%WG_FOLDER%\download_complete.txt"
