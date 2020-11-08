from fastapi import APIRouter
import requests
import json

router = APIRouter()

# route for getting bitcoin price
@router.get("/btc")
async def btc_summary():
    # TODO: find out why pycoingecko won't containerize to cloud run
    # request for current btc price in cad
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=cad')
    response.raise_for_status()

    # respond back with a json object
    return {"200" : json.loads(response.text)}