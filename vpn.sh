#!/bin/zsh
cd ~/code/python/openForti
source venv/bin/activate
sudo venv/bin/python main.py "$@"
