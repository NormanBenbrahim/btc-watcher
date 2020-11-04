from fastapi import FastAPI
import requests
app = FastAPI()

@app.get("/")
def home():
    return {"message":"oh yeah baby"}
