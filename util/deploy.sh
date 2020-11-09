#!/bin/bash

# project specific environment variables
export SERVICE_ACCT="fast-api"
export PROJECT_ID="watch-btc-dev"

# login to cloudrun instance
gcloud init

# configure
gcloud config set run/platform managed
gcloud config set run/region us-central1

# build the container
gcloud builds submit --tag eu.gcr.io/$PROJECT_ID/app