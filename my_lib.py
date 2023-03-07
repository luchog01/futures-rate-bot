from binance.client import Client
from datetime import date, datetime
import config
import json


client = Client(config.BinanceAPIKey, config.BinanceAPISecretKey)
expired_date = date(2023, 3, 31).strftime("%y%m%d")

def _daystoclose_():
    today = date.today()
    # strip the date from expired_date
    d0 = datetime.strptime(expired_date, '%y%m%d').date()
    days_to_close = d0 - today
    days_to_close = days_to_close.days
    return days_to_close

def _BTCUSD_ ():

    days_to_close = _daystoclose_()
    
    raw = client.get_recent_trades(symbol='BTCUSDT')
    BTCUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol=f"BTCUSD_{expired_date}")
    BTCUSDT_futures = float(raw[0]["price"])

    TNA = -((((BTCUSDT_spot/BTCUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("BTCUSD TNA = "+TNA) 

def _ETHUSD_ ():

    days_to_close = _daystoclose_()

    raw = client.get_recent_trades(symbol='ETHUSDT')
    ETHUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol=f"ETHUSD_{expired_date}")
    ETHUSDT_futures = float(raw[0]["price"])

    TNA = -((((ETHUSDT_spot/ETHUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("ETHUSD TNA = "+TNA)

def _ADAUSD_ ():

    days_to_close = _daystoclose_()

    raw = client.get_recent_trades(symbol='ADAUSDT')
    ADAUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol=f"ADAUSD_{expired_date}")
    ADAUSDT_futures = float(raw[0]["price"])

    TNA = -((((ADAUSDT_spot/ADAUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("ADAUSD TNA = "+TNA)

def _XRPUSD_ ():

    days_to_close = _daystoclose_()

    raw = client.get_recent_trades(symbol='XRPUSDT')
    XRPUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol=f"XRPUSD_{expired_date}")
    XRPUSDT_futures = float(raw[0]["price"])

    TNA = -((((XRPUSDT_spot/XRPUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("XRPUSD TNA = "+TNA)

def _BCHUSD_ ():

    days_to_close = _daystoclose_()

    raw = client.get_recent_trades(symbol='BCHUSDT')
    BCHUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol=f"BCHUSD_{expired_date}")
    BCHUSDT_futures = float(raw[0]["price"])

    TNA = -((((BCHUSDT_spot/BCHUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("BCHUSD TNA = "+TNA)

def _ETHUSD_ ():

    days_to_close = _daystoclose_()

    raw = client.get_recent_trades(symbol='ETHUSDT')
    ETHUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol=f"ETHUSD_{expired_date}")
    ETHUSDT_futures = float(raw[0]["price"])

    TNA = -((((ETHUSDT_spot/ETHUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("ETHUSD TNA = "+TNA)

