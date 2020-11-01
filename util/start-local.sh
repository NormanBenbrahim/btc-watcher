#!/bin/bash

venv="venv"

# if no venv folder, make sure user types the commands
if [ ! -d "$venv" ]; then
    echo "No virtual env executable found"
    echo "Please type the following commands first:"
    echo ""
    echo "python3 -m venv venv"
    echo "source venv/bin/activate"
    echo ""
    echo "Then re-run this file"
    exit
fi

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