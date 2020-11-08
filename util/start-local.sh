#!/bin/bash

if [ ! -d "$HOME/.pyenv/versions/3.8.6" ]; then
    pyenv install 3.8.6
    pyenv global 3.8.6
else 
    pyenv global 3.8.6
fi

# add specific version to the path
export PATH="~/.pyenv/versions/3.8.6/bin:${PATH}"

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

gunicorn -k uvicorn.workers.UvicornWorker --workers 4 --threads 8 --timeout 0 app/main:app