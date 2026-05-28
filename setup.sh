#!/bin/bash
echo 'Setting up AutoBugBountyHunter...'

# Install dependencies for Termux/Kali
if command -v pkg &> /dev/null; then
  pkg update && pkg install python git curl -y
  pip install requests rich colorama
else
  sudo apt update && sudo apt install python3-pip git curl -y
  pip3 install requests rich colorama
fi

echo 'Setup complete!'
chmod +x autobug.py