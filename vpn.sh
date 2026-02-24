#!/bin/zsh
cd ~/code/openForti
source venv/bin/activate
sudo venv/bin/python main.py "$@"
