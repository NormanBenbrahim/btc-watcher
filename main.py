from fastapi import FastAPI
import astroid
import Click==7.0
import colorama==0.4.3
import fastapi==0.47.1
import gunicorn==20.0.4
import h11==0.9.0
import isort==4.3.21
import lazy-object-proxy==1.4.3
import mccabe==0.6.1
import pydantic==1.4
import pylint==2.4.4
import six==1.14.0
import starlette==0.12.9
import uvicorn==0.11.2
import websockets==8.1
import requests==2.23.0
import wrapt==1.11.2
import tensorflow==2.3.0
import alpha_vantage==2.2.0

app = FastAPI()

@app.get("/")
def home():
    return {"message":"oh yeah baby"}
