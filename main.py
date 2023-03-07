import config
from binance.client import Client
from time import sleep
from datetime import date, datetime
import csv

client = Client(config.BinanceAPIKey, config.BinanceAPISecretKey)
treshold = 10

def TNA (symbol, expired_date):

    def _daystoclose_():
        today = date.today()
        # strip the date from expired_date
        d0 = datetime.strptime(expired_date, '%y%m%d').date()
        days_to_close = d0 - today
        days_to_close = days_to_close.days
        return days_to_close

    days_to_close = _daystoclose_()

    raw = client.get_recent_trades(symbol=symbol+"T")
    spot_price = float(raw[0]["price"])

    raw = client.futures_coin_symbol_ticker(symbol=f"{symbol}_{expired_date}")
    future_price = float(raw[0]["price"])

    TNA = round(-((((spot_price/future_price)-1)/days_to_close)*365)*100, 2)

    print(f"{symbol} TNA = {TNA}%")
    return TNA,spot_price,future_price

def main():
    while True:
        try:

            futures = client.futures_coin_exchange_info()["symbols"]

            with open("data.csv", "a", newline="", encoding="utf-8") as outfile:
                csv_writer = csv.writer(outfile)
                # if empty
                if outfile.tell() == 0:
                    csv_writer.writerow(["Time", "Symbol", "TNA", "Spot Price", "Future Price"])

            while True:
                for future in futures:
                    if future["contractType"] == "CURRENT_QUARTER":
                        symbol,expired_date = future["symbol"].split("_")
                        tna,spot_price,future_price = TNA(symbol,expired_date)
                        if tna > treshold:
                            # append time and symbol to txt
                            with open("data.csv", "a", newline="", encoding="utf-8") as outfile:
                                csv_writer = csv.writer(outfile)
                                csv_writer.writerow([datetime.now(), symbol, tna, spot_price, future_price])

        except:
            sleep(60)

if __name__ == "__main__":
    main()