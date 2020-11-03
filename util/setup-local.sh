#!/bin/bash

# ensure you work in same python version as on google cloud app engine
brew install pyenv && brew install pyenv-virtualenv
pyenv install 3.7.3
pyenv global 3.7.3
# add specific version to the path
export PATH="~/.pyenv/versions/3.7.3/bin:${PATH}"

# if no venv folder, make sure to create it 
if [ ! -d "venv" ]; then
    pyenv virtualenv 3.7.3 venv
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

# create env variable letting the app know it is running a local instance
export IS_LOCAL="1"
export IS_DEV="0"
export IS_PROD="0"

python main.py