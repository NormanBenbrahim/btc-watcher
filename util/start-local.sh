#!/bin/bash

venv="../venv"

# if no venv folder, make sure to create it 
if [ ! -d "$venv" ]; then
    python3 -m venv venv
fi

# TODO: add check for gcloud sdk

# some housekeeping 
if [ ! -z "${VIRTUAL_ENV}" ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "Please type 'source venv/bin/activate' first, then re-run this file"
    exit
fi

# make sure the google cloud credentials exist
if [ -z "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo "WARNING: Your Google API credentials file does not exist"
    echo "All Google Cloud products will not work"
fi

# create env variable letting the app know it is running a local instance
export IS_PRODUCTION="0"

python main.py