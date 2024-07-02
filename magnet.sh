#!/bin/bash

WG_FOLDER=$(dirname "$0")/wg

ARIA2C_EXE_PATH=aria2c
MAGNET_URL=$(cat "${WG_FOLDER}/magnetToDownload.txt")

DOWNLOAD_FOLDER=("${WG_FOLDER}/download")

"${ARIA2C_EXE_PATH}" --dir "${DOWNLOAD_FOLDER}" --enable-dht=true --bt-enable-lpd=true --enable-peer-exchange=true --dht-listen-port=6881-6999 --seed-time=0 --file-allocation=none --disable-ipv6 "${MAGNET_URL}" 

echo "Download complete!" > "${WG_FOLDER}/download_complete.txt"