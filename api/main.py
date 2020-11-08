from fastapi import FastAPI
from enum import Enum
import uvicorn
import logging
import requests
import json 
from routers import models, btc, health_check

# formatter for logging
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')

# start api
app = FastAPI()

# root route
@app.get("/")
async def home():
    return {"200": "Successfully connected to API, visit /docs to view all routes"}

# include routes
app.include_router(models.router)
app.include_router(btc.router)
app.include_router(health_check.router)

if __name__ == '__main__':
    uvicorn.run(app, debug=True, host="0.0.0.0", port=8000)