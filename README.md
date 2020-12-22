# Bitcoin Watcher

RestAPI to watch and collects useful data about BTC wrapped in a rest API built using Python (fastapi), delivered in a docker container hosted on Google Cloud Run

# Requirements

Docker and Python 3.8, see `requirements.txt` and `Dockerfile`

# Setup (one-time)

### Step 1

Create an account with TAAPI: https://taapi.io/

Then add this environment variable to your configuration: 
```
export TAAPI_KEY="key here"
```

### Step 2

Create a new email with gmail, then follow the guide here to get started authenticating with Gmail API: https://taapi.io/documentation/

Then add these environment variables to your configuration when you enable the API:
```
export GMAIL_CLIENT_ID="client id here"
export GMAIL_CLIENT_SECRET="client secret here"
```


### Step 3

Run the `start` scripts for your environment and follow instructions

**Local:** On a Mac (make sure homebrew is installed):

```
./tools/setup-local.sh
```

**Dev/Prod:** On Google App Engine it's the same concept

```
./tools/setup-dev.sh
```

# Usage 

### Launching the app

**Local:** On a Mac (make sure homebrew is installed):

```
./tools/start-local.sh
```

**Dev/Prod:** On Google App Engine it's the same concept

```
./tools/start-dev.sh
```