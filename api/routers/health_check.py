from fastapi import APIRouter
from datetime import datetime 
from pytz import timezone 

router = APIRouter()

# route for healthcheck
@router.get("/health-check")
async def healthcheck():
    # collect info for response
    uptime = datetime.now(timezone('EST')) - start_time
    uptime = uptime.total_seconds()
    message = 'OK'
    timestamp = datetime.now(timezone('EST'))
    out_timestamp = timestamp.strftime('%m/%d/%Y, %H:%M:%S')

    # return response
    return {"uptime (seconds)": uptime, "message": message, "timestamp": out_timestamp}