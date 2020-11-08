# Bitcoin Watcher

RestAPI to watch and collects useful data about BTC wrapped in a rest API built using Python (fastapi), delivered in a docker container hosted on Google Cloud Run

# Requirements

Python 3.8, see `requirements.txt` and `Dockerfile`

# Setup (one-time)

### Step 1
```
git clone https://github.com/NormanBenbrahim/mind-med-watcher.git
cd mind-med-watcher
./util/setup-local.sh OR ./util/setup-gcp.sh
```


### Step 2

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