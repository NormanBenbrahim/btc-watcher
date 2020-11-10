import math
from enum import Enum
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
from fastapi import APIRouter
import json 
import requests
from datetime import datetime 
from pytz import timezone 
from dateutil.relativedelta import relativedelta

router = APIRouter()

NUM_EPOCHS = 480
BATCH_SIZE = 160

# based on this paper: 
# https://www.researchgate.net/publication/328989226_Machine_Learning_Models_Comparison_for_Bitcoin_Price_Prediction
# in the paper, 1-minute interval trading exchange data rate in USD from January 1 2012 to January 8, 2018 (6 years) is focused

# run the model fresh on new data from the past {X} months
@router.get("/predict/{number_of_months}")
async def predict_price(number_of_months):
    """
    Run GRU model fresh on new data from the past {X} months to predict BTC price in one hour from start time
    """
    # get unix timestamps
    time_now = datetime.now(timezone('EST'))

    # time {X} months ago
    time_x_months_ago = time_now + relativedelta(months=-number_of_months)

    # gather url to make request
    base_url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=cad&'
    filter_url = f'from={time_x_months_ago.timestamp()}&to={time_now.timestamp()}'
    request_url = base_url + filter_url

    request = requests.get(request_url)

    # TODO: setup Xtrain and Ytrain 70/30 split from btc prices on coingecko
    Xtrain, Ytrain = None, None
    Xtest, Ytest = None, None

    # prepare the data
    train_size = (Xtrain.shape[0] // BATCH_SIZE) * BATCH_SIZE
    test_size = (Xtest.shape[0] // BATCH_SIZE) * BATCH_SIZE

    Xtrain, Ytrain = Xtrain[0:train_size], Ytrain[0:train_size]
    Xtest, Ytest = Xtest[0:test_size], Ytest[0:test_size]

    # setup & compile the model
    model = Sequential()
    model.add(GRU(231, input_shape=(1,4), go_backwards=True,
                  activation='relu', return_sequences=False))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error'])

    # fit model
    for i in range(NUM_EPOCHS):
        model.fit(Xtrain, Ytrain, batch_size=BATCH_SIZE, epochs=1,
                  validation_data=(Xtest, Ytest), shuffle=False, verbose=0)

    # get metrics
    score, _ = model.evaluate(Xtest, Ytest, batch_size=BATCH_SIZE, verbose=0)
    rmse = math.sqrt(score)

    return {200: "done"}