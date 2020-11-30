from fastapi import APIRouter
from datetime import datetime 
from pytz import timezone 
import os 

api_key = os.environ['IEX_KEY']

router = APIRouter()

# start the timer for the health check, convert to est timezone
start_time = datetime.now(timezone('EST'))

@router.get('/alerter')
async def alerter():
    return {"message": "ok"}