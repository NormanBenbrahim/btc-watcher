import astroid
import click
import colorama
import fastapi
import gunicorn
import h11
import isort
import lazy_object_proxy
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

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"oh yeah baby"}
