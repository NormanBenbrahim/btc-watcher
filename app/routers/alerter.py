from fastapi import APIRouter
from datetime import datetime 
from pytz import timezone 
import requests
import os 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# taapi key (for indicators)
taapi_key = os.environ['TAAPI_KEY']
taapi_base_url = "https://api.taapi.io"

# binance key (for price action)
binance_key = os.environ["BINANCE_API_KEY"]
binance_private_key = os.environ["BINANCE_SECRET_KEY"]

# for sending a message through telegram
telegram_token = os.environ["TELEGRAM_TOKEN"]
telegram_chat = os.environ["TELEGRAM_CHAT"]
telegram_base_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={telegram_chat}&text="

# initiate the router
router = APIRouter()

def send_telegram(text):
    out_text = text.replace(' ', '+')
    api_url = telegram_base_url + out_text
    send_msg = requests.get(api_url)
    send_msg.raise_for_status()
    return "Message sent"


def indicator_call(api_url, params, indicators):
    try:
        # initialize indicator output
        output_indicators = {}

        # request session to handle multiple calls without authenticating every time
        with requests.Session() as session:
            for indicator in indicators:
                # build the url
                indicator_url = api_url + '/' + indicator
                
                # make the request and ensure status 200
                response = session.get(url=indicator_url, params=params, timeout=60)
                response.raise_for_status()

                # collect the indicator
                #print(response.json())
                value = response.json()['value']
                output_indicators[indicator] = value
        
        return output_indicators

    except TimeoutError:
        print(f"Timeout! URL: {api_url}")

# main route
@router.get('/btc_indicators')
async def btc_indicators():
    # setup params for api call to taapi
    parameters = {
        'secret': taapi_key,
        'exchange': 'binance',
        'symbol': 'BTC/USDT',
        'interval': '1h'
        } 
    
    # make the call
    indicators = ['rsi', 'mfi', 'stochrsitv']
    values = indicator_call(taapi_base_url, parameters, indicators)

    # set the output variables for the response
    rsi = values['rsi']
    mfi = values['mfi']
    stochK = values['stochrsitv']['valueK']
    stochD = values['stochrsitv']['valueD']

    # check the conditions set by the trading plan
    # first the singular conditions
    alert = False
    if rsi < 35:
        send_telegram(f"[BTC ALERT] RSI just dipped below 35 in the 1h timeframe, data below")
        send_telegram(f"[BTC ALERT] RSI={rsi}, 52-week-high={1}, PriceNow={1}")
        alert = True

    if mfi < 21:
        send_telegram(f"[BTC ALERT] MFI just dipped below 21 in the 1h timeframe, data below")
        send_telegram(f"[BTC ALERT] MFI={mfi}, 52-week-high={1}, PriceNow={1}")
        alert = True

    if stochD < 21 or stochK < 21:
        send_telegram(f"[BTC ALERT] StochRSI just dipped below 21 in the 1h timeframe, data below")
        send_telegram(f"[BTC ALERT] StochRSI(K)={stochK}, StochRSI(D)={stochD}, 52-week-high={1}, PriceNow={1}")
        alert = True

    # now the mixed conditions
    if rsi < 35 and mfi < 21:
        send_telegram(f"[!BTC ALERT] BOTH RSI and MFI conditions met, data below")
        send_telegram(f"")
        alert = True

    if rsi < 35 and (stochD < 21 or stochK < 21):
        send_telegram(f"[!BTC ALERT] BOTH RSI and StochRSI conditions met, data below")
        send_telegram(f"[!BTC ALERT] RSI={rsi}, StochRSI(K)={stochK}, StochRSI(D)={stochD}, 52-week-high={1}, PriceNow={1}")
        alert = True

    if mfi < 21 and (stochD < 21 or stochK < 21):
        send_telegram(f"[!BTC ALERT] BOTH MFI and StochRSI conditions met, data below")
        send_telegram(f"[!BTC ALERT] MFI={mfi}, StochRSI(K)={stochK}, StochRSI(D)={stochD}, 52-week-high={1}, PriceNow={1}")
        alert = True

    # the big one, if all conditions are met
    if mfi < 21 and rsi < 35 and (stochD < 21 or stochK < 21):
        send_telegram(f"[!!BIG BTC ALERT!!] ALL INDICATORS FIT CONDITIONS, data below")
        send_telegram(f"[!!BIG BTC ALERT!!] RSI={rsi}, MFI={mfi}, StochRSI(K)={stochK}, StochRSI(D)={stochD}, 52-week-high={1}, PriceNow={1}")
        alert = True

    output = {"alert?" : alert, "RSI": rsi, "MFI": mfi, "StochRSI(K)": stochK, "StochRSI(D)": stochD}

    return output