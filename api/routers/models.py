import math
from enum import Enum
from tensorflow.keras.initializers import lecun_uniform
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
from fastapi import APIRouter
import json 
import requests

router = APIRouter()

NUM_EPOCHS = 480
BATCH_SIZE = 160

# setup the model
class ModelName(str, Enum):
    theilsen = "theilsen"
    huber = "huber"
    lstm = "lstm"
    gru = "gru"

# based on this paper: 
# https://www.researchgate.net/publication/328989226_Machine_Learning_Models_Comparison_for_Bitcoin_Price_Prediction
# in the paper, 1-minute interval trading exchange data rate in USD from January 1 2012 to January 8, 2018 (6 years) is focused

# run the model fresh on new data
@router.get("/models", tags=['models'])
async def get_model(model_name: ModelName):
    if model_name == ModelName.theilsen:
        return {"model_name": model_name, "message": "Theilsen model selected"}

    if model_name.value == "huber":
        return {200: model_name, "message": "Huber model selected"}

    if model_name.value == "lstm":
        return {200: model_name, "message": "LSTM model selected"}

    # gru model
    model = Sequential()
    model.add(GRU(231, input_shape=(1,4), go_backwards=True,
                  activation='relu', return_sequences=False))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error'])
    return {200: "gru"}