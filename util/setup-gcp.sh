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
echo "creating cloudrun service"
gcloud config set project watch-mmed-dev 
gcloud builds submit --tag gcr.io/watch-mmed-dev.io/ 
gcloud run --platform="managed" --region="us-central1"
gcloud secrets create fast-api-v1 --replication-policy="automatic"
gcloud secrets versions add fast-api-v1 --data-file=".env"