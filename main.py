from fastapi import FastAPI
import astroid
import Click
import colorama
import fastapi
import gunicorn
import h11
import isort
import lazy-object-proxy
import mccabe
import pydantic
import pylint
import six
import starlette
import uvicorn
import websockets
import requests
import wrapt
import tensorflow
import alpha_vantage

app = FastAPI()

@app.get("/")
def home():
    return {"message":"oh yeah baby"}
