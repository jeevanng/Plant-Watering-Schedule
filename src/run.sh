#! /bin/bash

if [ -d "./.venv" ]; then
    echo "The virtual environment already exists. Please wait a moment for it to activate..."
    source .venv/bin/activate
else
    echo "The virtual environment does not exist. Please wait a moment for it to create and activate..."
    python3 -m venv .venv
    source .venv/bin/activate
fi

pip3 install -r requirements.txt 
clear
python3 main.py 
