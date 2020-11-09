from fastapi import APIRouter
#from google.cloud import datastore
#import requests

router = APIRouter()

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