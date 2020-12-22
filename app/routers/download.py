from fastapi import APIRouter
from datetime import datetime
from time import sleep
from pytz import timezone
from dateutil.relativedelta import relativedelta
import requests
from firebase_admin import credentials, firestore, initialize_app
from starlette.requests import Request
from pandas import date_range, Series, concat
from itertools import tee, islice, chain

# initialize the router
router = APIRouter()

# initialize the database object
#initialize_app(name="btc-app")
#db = firestore.client()
#collection = db.collection('features')

# helper functions
def chunks(lst, n):
    """Yield successive n-sized chunks from a list."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def previous_and_next(some_iterable):
    """Iterate through your list, dict, or whatever iterable and give access to current, 
    prev and next elements"""
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)

def make_request(number_months):
    """Make API calls to coingecko respecting their rate limit (10 calls per second)"""
    # timestamps 
    time_now = datetime.now()
    time_n_months_ago = time_now + relativedelta(months=-number_months)

    # get a list of timestamps spaced out by 5 minute chunks
    time_5min_intervals = date_range(time_n_months_ago, time_now, freq='5min')
    
    # now loop through each element in the list, and make request from the start time (first element) 
    # to the end time (last element)
    base_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=cad&"
    price_list = []
    number_requests_made = 0
    for previous, item, nxt in previous_and_next(time_5min_intervals):
        if number_requests_made > 10:
            print("exceeded number of calls made allowed per second, pausing for 3 seconds")
            sleep(3)
            print("continuing")
            number_requests_made = 0

        t1, t2 = item.timestamp(), nxt.timestamp()
        filter_url = f"from={t1}&to={t2}"

        # make the request and add to request count
        url = base_url + filter_url
        print(f"url: {url}")
        print(f"regular times t1: {item}, t2: {nxt}")
        print(f"timestamps: t1: {item.timestamp()} t2: {nxt.timestamp()}")
        req = requests.get(url)
        req.raise_for_status()
        number_requests_made += 1

        # process the raw json data
        raw_data = req.json()
        print(f"request: {raw_data}")
        data = raw_data['prices']
        prices = [x[1] for x in data]

        # build a series for the given timeframe
        #miniseries = Series(prices, index=time)

        # append series to main list
        price_list.append(prices)
    
    # concat the timeseries together
    all_prices = concat(price_list)

    return all_prices



@router.get("/download")
async def download(number_months: int, request: Request):
    """
    Download minutely data (in CAD) for specified number of months
    """
    all_prices = make_request(number_months)

    return {'all_prices': all_prices}