from fastapi import APIRouter
from google.cloud import datastore
import requests

router = APIRouter()

# start datastore client
ds_client = datastore.Client()
KEY_TYPE = 'Record'

# datastore put/update & get functions
def insert(**data):
    entity = datastore.Entity(key=ds_client.key(KEY_TYPE))
    entity.update(**data)
    ds_client.put(entity)

def query(limit):
    return ds_client.query(kind=KEY_TYPE).fetch(limit=limit)

# download route
@router.get('/download', tags='download')
async def download():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=cad')
    response.raise_for_status()
    return {200: "done"}