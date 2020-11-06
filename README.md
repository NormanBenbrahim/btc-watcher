# Mindmed Watcher

Watches the stock MindMed (MMED) and collects useful data about the stock wrapped in a rest API built using Python (fastapi), delivered in a docker container hosted on Google Cloud Run

# Requirements

Python 3.7.3, see `requirements.txt`

# Setup (one-time)

### Step 1
Get the free API keys:

* https://www.alphavantage.co/

Then change the following line inside `.env-example` and rename the file to `.env`:
```
ALPHA_VANTAGE_KEY="your api key"
```

### Step 2
```
git clone https://github.com/NormanBenbrahim/mind-med-watcher.git
cd mind-med-watcher
./util/setup-local.sh OR ./util/setup-gcp.sh
```


### Step 3

Run the `start` scripts for your environment and follow instructions

**Local:** On a Mac (make sure homebrew is installed):

```
./util/setup-local.sh
```

**Dev/Prod:** On Google App Engine it's the same concept

```
./util/setup-dev.sh
```

# Usage 

### Launching the app

**Local:** On a Mac (make sure homebrew is installed):

```
./util/start-local.sh
```

**Dev/Prod:** On Google App Engine it's the same concept

```
./util/start-dev.sh
```