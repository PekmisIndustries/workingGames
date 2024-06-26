@echo off
setlocal

rem Set variables
set WG_FOLDER=%~dp0wg
set /p ARIA2C_EXE_PATH<"%WG_FOLDER%\ariaPath.txt"
set DOWNLOAD_FOLDER=%WG_FOLDER%\download

rem Convert DOWNLOAD_FOLDER path if needed
set DOWNLOAD_FOLDER_WINDOWS=%DOWNLOAD_FOLDER%

rem Read magnet link from file
set /p MAGNET_URL=<"%WG_FOLDER%\magnetToDownload.txt"

rem Remove line breaks from magnet link
set "MAGNET_URL=%MAGNET_URL:\\=\%"
set "MAGNET_URL=%MAGNET_URL:\=\\%"
set "MAGNET_URL=%MAGNET_URL:&=^&%"
set "MAGNET_URL=%MAGNET_URL:|=^|%"
set "MAGNET_URL=%MAGNET_URL:<=^<%"
set "MAGNET_URL=%MAGNET_URL:>=^>%"
set "MAGNET_URL=%MAGNET_URL:/=^/%"

rem Run aria2c
echo %MAGNET_URL%
"%ARIA2C_EXE_PATH%" "%MAGNET_URL%" --seed-time --dir "%DOWNLOAD_FOLDER_WINDOWS%"

rem Write download complete indicator
echo Download complete! > "%WG_FOLDER%\download_complete.txt"
pause
goto :eof