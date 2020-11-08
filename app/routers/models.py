import math
from enum import Enum
from tensorflow.keras.initializers import lecun_uniform
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
from fastapi import APIRouter

router = APIRouter()

# setup the model
class ModelName(str, Enum):
    theilsen = "theilsen"
    huber = "huber"
    lstm = "lstm"
    gru = "gru"

# based on this paper: 
# https://www.researchgate.net/publication/328989226_Machine_Learning_Models_Comparison_for_Bitcoin_Price_Prediction

# route for model selection
@router.get("/models")
async def get_model(model_name: ModelName):
    if model_name == ModelName.theilsen:
        return {"model_name": model_name, "message": "Theilsen model selected"}

    if model_name.value == "huber":
        return {"model_name": model_name, "message": "Huber model selected"}

    if model_name.value == "lstm":
        return {"model_name": model_name, "message": "LSTM model selected"}

    return {"model_name": model_name, "message": "GRU model selected"}