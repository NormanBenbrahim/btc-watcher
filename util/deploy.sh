#!/bin/bash

export PROJECT_ID="watch-mmed-dev"

# login to cloudrun instance
gcloud init

# configure
gcloud config set run/platform managed
gcloud config set run/region europe-west43

# build the container
gcloud builds submit --tag eu.gcr.io/$PROJECT_ID/app