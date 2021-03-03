#!/usr/bin/bash

BLUE='\033[34;4m'
WHITE='\033[0m'

if [[ $EUID -ne 0 ]]; then
	echo "Please run it as root"
	exit 1
fi

apt-get update && apt-get install termit
chmod +x main.py
cp main.py ratloader && mv ratloader /usr/bin

