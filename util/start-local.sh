#!/bin/bash

# set the google cloud project
gcloud config set project watch-mind-med

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
export IS_LOCAL="1"
export IS_DEV="0"
export IS_PROD="0"

gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app