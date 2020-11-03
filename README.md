# Mindmed Watcher

Watches the stock MindMed (MMED) and collects useful data about the stock wrapped in a rest API built using Python (fastapi)

# Requirements

Python 3.7.3 & Homebrew, see `requirements.txt` for package requirements

# Setup

Clone the repo and `cd` into it, then:

On a Mac (make sure homebrew is installed):

```
git clone https://github.com/NormanBenbrahim/mind-med-watcher.git
cd mind-med-watcher
./util/setup-local.sh
```
Then follow instructions. The prompts will let you know when you're ready to run your instance's `start` script

On Google App Engine it's the same concept (for dev)
```
git clone https://github.com/NormanBenbrahim/mind-med-watcher.git
cd mind-med-watcher
./util/setup-dev.sh
```

# Usage 

Launch the API

```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```