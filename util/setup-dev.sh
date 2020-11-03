#!/bin/bash

# this will prompt you to answer some stuff on the terminal
sudo apt update && sudo apt upgrade --fix-missing

# create env variable letting the app know it is running a local instance
export IS_LOCAL="0"
export IS_DEV="1"
export IS_PROD="0"