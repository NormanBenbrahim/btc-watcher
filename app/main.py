from datetime import datetime
from fastapi import FastAPI
from enum import Enum
import logging

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

# TODO: route for mmed current price
#ts = TimeSeries(key='YOUR_API_KEY')
# Get json object with the intraday data and another with  the call's metadata
#data, meta_data = ts.get_intraday('GOOGL')

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
async def home():
    try:
        # collect info for response
        uptime = datetime.now() - start_time
        uptime = uptime.total_seconds()
        message = 'OK'
        timestamp = datetime.now()

        # return response
        return {"uptime": uptime, "message": message, "timestamp": timestamp}
    
    except Exception as e:
        print(e)

