from datetime import datetime
from typing import Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging

# set the formatter for logging later
#formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')

# start api
app = FastAPI()

# start the timer for the health check
start_time = datetime.now()

@app.put("/health-check")
def home():
    try:
        # collect info for response
        uptime = datetime.now() - start_time
        uptime = uptime.total_seconds()
        message = 'OK'
        timestamp = datetime.now()

        # make a json object
        response = jsonable_encoder({"uptime": uptime,
                                     "message": message,
                                     "timestamp": timestamp})

        # return the json object
        return JSONResponse(content=response)
    
    except Exception as e:
        print(e)