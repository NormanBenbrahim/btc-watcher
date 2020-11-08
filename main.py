from datetime import datetime
from pytz import timezone
from fastapi import FastAPI
from enum import Enum
import uvicorn
import logging
import requests
import json 

# formatter for logging
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')

# start the timer for the health check, convert to est timezone
start_time = datetime.now(timezone('EST'))

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
    return {"200": "Successfully connected to API, visit /docs to view all routes"}

# route for getting bitcoin price
@app.get("/btc")
async def btc_summary():
    # TODO: find out why pycoingecko won't containerize to cloud run
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=cad')
    response.raise_for_status()

    # respond back with a json object
    return {"200" : json.loads(response.text)}

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
    uptime = datetime.now(timezone('EST')) - start_time
    uptime = uptime.total_seconds()
    message = 'OK'
    timestamp = datetime.now(timezone('EST'))
    out_timestamp = timestamp.strftime('%m/%d/%Y, %H:%M:%S')

    # return response
    return {"uptime (seconds)": uptime, "message": message, "timestamp": out_timestamp}

if __name__ == '__main__':
    uvicorn.run(app, debug=True, host="0.0.0.0", port=8000)