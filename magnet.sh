#!/bin/bash

WG_FOLDER=$(dirname "$0")/wg

ARIA2C_EXE_PATH=aria2c
MAGNET_URL=$(cat "${WG_FOLDER}/magnetToDownload.txt")

DOWNLOAD_FOLDER=("${WG_FOLDER}/download")

"${ARIA2C_EXE_PATH}" --seed-time -d "${MAGNET_URL}" --dir "${DOWNLOAD_FOLDER}" 

echo "Download complete!" > "${WG_FOLDER}/download_complete.txt"