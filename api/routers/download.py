from fastapi import APIRouter
from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta
import requests

router = APIRouter()

# get time objects
time_now = datetime.now(timezone('EST'))
time_three_months_ago = time_now + relativedelta(months=-3)

@router.get('/download')
async def download():
    """
    Route to download the last 3 months of bitcoin data to google cloud 
    """
    #response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=cad')
    #response.raise_for_status()
    return {200: "done"}


@router.get('/download/{months}')
async def download_last_months(months):
    """
    Route to download the last {X} months of bitcoin data to google cloud 
    """

    return {200: str(months)}