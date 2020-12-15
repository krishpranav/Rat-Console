#!bin/bash

echo "Installing Dependencies and python modules"
python3 -m pip install -r requirements.txt
sudo chmod +x console.py
clear
echo "Now you can run python3 console.py"