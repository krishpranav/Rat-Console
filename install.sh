#!bin/bash

echo "Installing Dependencies and python modules"
python3 -m pip install -r requirements.txt
sudo chmod +x console.py
clear
echo "Now You Can Run python3 console.py"
