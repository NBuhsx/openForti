#!/bin/zsh
cd ~/Code/openForti
source venv/bin/activate
sudo venv/bin/python3.11 main.py "$@"
