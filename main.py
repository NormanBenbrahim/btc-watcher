from fastapi import FastAPI
#import tensorflow as tf
app = FastAPI()

@app.get("/")
def home():
    return {"message":"oh yeah baby"}
