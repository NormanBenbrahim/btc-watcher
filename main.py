from datetime import datetime
from fastapi import FastAPI
from enum import Enum
from pycoingecko import CoinGeckoApi
import os 
import logging

# formatter for logging
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')

# start the timer for the health check
# TODO: add conversion from UTC to EST time for all times in script
start_time = datetime.now()

# setup the model
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# start api
app = FastAPI()

# root route
@app.get("/")
async def home():
    return {"200": "Successfully connected to API, visit '/docs' to view all routes"}

# route for getting bitcoin price
@app.get("/btc")
async def btc_summary():
    cg = CoinGeckoAPI()
    btc = cg.get_price(ids='bitcoin', vs_currencies='cad')
    return {"200": btc}

# route for choosing a model
@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# route for healthcheck
@app.get("/health-check")
async def healthcheck():
    # collect info for response
    uptime = datetime.now() - start_time
    uptime = uptime.total_seconds()
    message = 'OK'
    timestamp = datetime.now()

    # return response
    return {"uptime": uptime, "message": message, "timestamp": timestamp}