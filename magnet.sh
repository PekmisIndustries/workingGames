#!/bin/bash

DOWNLOAD_FOLDER=$(cat downloadFolderPath.txt)
ARIA2C_EXE_PATH=$(cat ariaPath.txt)
MAGNET_URL=$(cat magnetToDownload.txt)

"$ARIA2C_EXE_PATH" --seed-time -d "$DOWNLOAD_FOLDER" "$MAGNET_URL"