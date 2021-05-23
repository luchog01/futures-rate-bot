from binance.client import Client
from datetime import date
from time import sleep
import pyrebase
from config import configs
config_data = configs()

firebase = pyrebase.initialize_app(config_data.FireBaseconfig)
db = firebase.database()

client = Client(config_data.BinanceAPIKey, config_data.BinanceAPISecretKey)

def _daystoclose_():
    today = date.today()
    d0 = date(2021, 6, 25)
    days_to_close = d0 - today
    days_to_close = days_to_close.days
    return days_to_close

def _BTCUSD_ ():

    days_to_close = _daystoclose_()
    
    raw = client.get_recent_trades(symbol='BTCUSDT')
    BTCUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol="BTCUSD_210625")
    BTCUSDT_futures = float(raw[0]["price"])

    TNA = -((((BTCUSDT_spot/BTCUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("BTCUSD TNA = "+TNA)
    db.child("Trading Bots").child("Spot_Futures TNA").update({"BTCUSDT TNA":TNA})  

def _ETHUSD_ ():

    days_to_close = _daystoclose_()

    raw = client.get_recent_trades(symbol='ETHUSDT')
    ETHUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol="ETHUSD_210625")
    ETHUSDT_futures = float(raw[0]["price"])

    TNA = -((((ETHUSDT_spot/ETHUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("ETHUSD TNA = "+TNA)
    db.child("Trading Bots").child("Spot_Futures TNA").update({"ETHUSDT TNA":TNA})

def _ADAUSD_ ():

    days_to_close = _daystoclose_()

    raw = client.get_recent_trades(symbol='ADAUSDT')
    ADAUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol="ADAUSD_210625")
    ADAUSDT_futures = float(raw[0]["price"])

    TNA = -((((ADAUSDT_spot/ADAUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("ADAUSD TNA = "+TNA)
    db.child("Trading Bots").child("Spot_Futures TNA").update({"ADAUSDT TNA":TNA})

def _XRPUSD_ ():

    days_to_close = _daystoclose_()

    raw = client.get_recent_trades(symbol='XRPUSDT')
    XRPUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol="XRPUSD_210625")
    XRPUSDT_futures = float(raw[0]["price"])

    TNA = -((((XRPUSDT_spot/XRPUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("XRPUSD TNA = "+TNA)
    db.child("Trading Bots").child("Spot_Futures TNA").update({"XRPUSDT TNA":TNA})

def _BCHUSD_ ():

    days_to_close = _daystoclose_()

    raw = client.get_recent_trades(symbol='BCHUSDT')
    BCHUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol="BCHUSD_210625")
    BCHUSDT_futures = float(raw[0]["price"])

    TNA = -((((BCHUSDT_spot/BCHUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("BCHUSD TNA = "+TNA)
    db.child("Trading Bots").child("Spot_Futures TNA").update({"BCHUSDT TNA":TNA})

def _ETHUSD_ ():

    days_to_close = _daystoclose_()

    raw = client.get_recent_trades(symbol='ETHUSDT')
    ETHUSDT_spot = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol="ETHUSD_210625")
    ETHUSDT_futures = float(raw[0]["price"])

    TNA = -((((ETHUSDT_spot/ETHUSDT_futures)-1)/days_to_close)*365)*100
    TNA = str(round(TNA,2)) + "%"

    print("ETHUSD TNA = "+TNA)
    db.child("Trading Bots").child("Spot_Futures TNA").update({"ETHUSDT TNA":TNA})

