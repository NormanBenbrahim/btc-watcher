#!/bin/bash

# ensure you have the latest linux
sudo apt update && sudo apt -y upgrade --fix-missing

# make sure the right
if [ ! -d "venv" ]; then
    echo ""
    echo "Local virtual environment not found, creating..."
    virtualenv venv
fi

# must be working in a virtual environment
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

# NEVER give app owner role in prod, that's a nono. this is only fine in dev
echo "WARNING: setting up the environment for dev, this gives owner access to service account"
gcloud projects create watch-mind-med
gcloud iam service-accounts create api-dev-v1
gcloud projects add-iam-policy-binding mind --member="serviceAccount:api-dev-v1@watch-mind-med.iam.gserviceaccount.com" --role="roles/owner"
gcloud iam service-accounts enable apiv1@watch-mind-med.iam.gserviceaccount.com