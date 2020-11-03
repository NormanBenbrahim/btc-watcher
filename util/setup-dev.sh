#!/bin/bash

# comment this line out after running it the first time
sudo apt update --fix-missing

if [ ! -d "venv" ]; then
    echo ""
    echo "Local virtual environment not found, creating..."
    virtualenv venv
fi

# some housekeeping 
if [ ! -z "${VIRTUAL_ENV}" ]; then
    pip install -r requirements.txt
else
    echo ""
    echo "Please type 'source venv/bin/activate' first, then re-run this file"
    exit
fi

# create env variable letting the app know it is running a local instance
export IS_LOCAL="0"
export IS_DEV="1"
export IS_PROD="0"