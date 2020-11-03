#!/bin/bash

# ensure you work in same python version as on google cloud app engine
# comment these lines out when you run it the first time, otherwise it's annoying
brew install pyenv
brew install pyenv-virtualenv

echo "" 
echo ""

if [ ! -d "$HOME/.pyenv/versions/3.7.3" ]; then
    pyenv install 3.7.3
    pyenv local 3.7.3
else 
    pyenv local 3.7.3
fi

# add specific version to the path
export PATH="~/.pyenv/versions/3.7.3/bin:${PATH}"

# if no venv folder, make sure to create it 
if [ ! -d "venv" ]; then
    echo ""
    echo "Local virtual environment not found, creating..."
    python3 -m venv venv
fi

# some housekeeping 
if [ ! -z "${VIRTUAL_ENV}" ]; then
    pip install -r requirements.txt
else
    echo ""
    echo "Please type 'source venv/bin/activate' first, then re-run this file"
    exit
fi

# TODO: add check for gcloud sdk
if [ ! -d "$HOME/google-cloud-sdk" ]; then 
    echo "" 
    echo "The google cloud SDK is not installed, go here"
    echo "https://cloud.google.com/sdk/docs/install"
    echo "and install it first, then re-run this file"
    exit
else 
    gcloud auth login
fi 

# create env variable letting the app know it is running a local instance
export IS_LOCAL="1"
export IS_DEV="0"
export IS_PROD="0"

echo ""
echo ""
echo "***You are ready to work in your local instance!***"
echo "To start the app, type gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app"