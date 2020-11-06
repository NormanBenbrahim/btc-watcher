#!/bin/bash

# virtual environment
if [ ! -d "venv" ]; then
    echo ""
    echo "Local virtual environment not found, creating..."
    virtualenv venv
fi

# must be working in a virtual environment
if [ ! -z "${VIRTUAL_ENV}" ]; then
    pip install -r requirements.txt
else
    echo "Not working in venv"
    echo "Please type 'source venv/bin/activate' first, then re-run this file"
    exit
fi

# create the app
echo ""
echo "creating app"
gcloud app create --region=asia-south1

# create env variable letting the app know it is running a local instance
export IS_LOCAL="0"
export IS_DEV="1"
export IS_PROD="0"