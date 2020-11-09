from fastapi import APIRouter
from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta
import requests

router = APIRouter()

@router.get('/download')
async def download_last_3_months():
    """
    Route to download the last 3 months of bitcoin data to google cloud
    with hourly tickers

    RETURNS
        JSON object containing collection of [market cap, price]
    """
    # get timestamps
    time_now = datetime.now(timezone('EST'))
    time_three_months_ago = time_now + relativedelta(months=-3)

    # build request url
    base_url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=cad&'
    endpoint_url = f"from={time_three_months_ago.timestamp()}&to={time_now.timestamp()}"
    request_url = base_url + endpoint_url 
    
    # handle response
    response = requests.get(request_url)
    response.raise_for_status()
    
    # spit it back
    return response.json()


@router.get('/download/{n_months}')
async def download_last_X_months(n_months: int):
    """
    Route to download the last {n_months} months of bitcoin data to google cloud
    with hourly tickers

    PARAMS 
        months: number of months to go backwards (keep in mind cryptocurrencies were created
                in 2009)

    RETURNS
        JSON object containing collection of [market cap, price]
    """
    # get timestamps
    time_now = datetime.now(timezone('EST'))
    time_three_months_ago = time_now + relativedelta(months=-n_months)

    # build request url
    base_url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=cad&'
    endpoint_url = f"from={time_three_months_ago.timestamp()}&to={time_now.timestamp()}"
    request_url = base_url + endpoint_url 
    
    # handle response
    response = requests.get(request_url)
    response.raise_for_status()
    
    # spit it back
    return response.json()