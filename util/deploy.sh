#!/bin/bash

export PROJECT_ID="watch-btc-dev"

# login to cloudrun instance
gcloud init

# configure
gcloud config set run/platform managed
gcloud config set run/region europe-west43

# build the container
gcloud builds submit --tag eu.gcr.io/$PROJECT_ID/app