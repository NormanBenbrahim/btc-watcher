# Bitcoin Watcher

RestAPI to watch and collects useful data about BTC wrapped in a rest API built using Python (fastapi), delivered in a docker container hosted on Google Cloud Run

# Requirements

Docker and Python 3.8, see `requirements.txt` and `Dockerfile`

# Setup (one-time)

### Step 1

Create an account with TAAPI: https://taapi.io/

Then add this environment variable to your configuration (bash_profile/bashrc): 
```
export TAAPI_KEY="key here"
```

### Step 2

Create an account with Binance: https://www.binance.com/en and get your API key & secret.

Then add these environment variables to your configuration (bash_profile/bashrc):
```
export BINANCE_API_KEY="add api key here
export BINANCE_SECRET_KEY="add api secret here"
```


### Step 3

Test the app locally and make sure endpoints work on your computer (create a python 3.7.3 virtual environment first and source it)

```
pip install -r requirements.txt
python app/main.py
```


# Launching the app on GCP

Launch to Cloud Run and schedule it to run every 10 mins (or however often you want) with Cloud Scheduler

First add your API keys using Secret Manager (https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create_a_secret). Make sure to enable the IAM permission for the secret manager as well.

Then create a Cloud Run service, add the dockerfile in the directory, and add a trigger to CloudBuild to update everytime your `main` branch is updated