from fastapi import FastAPI
from enum import Enum
import uvicorn
import logging
import requests
import json
from routers import models, download, health_check

# formatter for logging
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')

# start api
app = FastAPI()

# root
@app.get("/")
async def root():
    return {200: "Successfully connected to API, visit /docs to view all routes"}

# include all other routes
app.include_router(models.router)
app.include_router(download.router)
app.include_router(health_check.router)

if __name__ == '__main__':
    uvicorn.run(app, debug=True, host="0.0.0.0", port=8000)