#!/bin/bash

WG_FOLDER=$(dirname "$0")/wg

ARIA2C_EXE_PATH=$(cat "${WG_FOLDER}/ariaPath.txt" | sed 's/\\/\//g')
MAGNET_URL=$(cat "${WG_FOLDER}/magnetToDownload.txt")

DOWNLOAD_FOLDER=$(cygpath -u "${WG_FOLDER}/download")

"${ARIA2C_EXE_PATH}" --seed-time -d "${MAGNET_URL}" --dir "${DOWNLOAD_FOLDER}" 

echo "Download complete!" > "${WG_FOLDER}/download_complete.txt"