import mysql.connector
from conn_util import *
import requests
from db_handler import DBHandler
import json
from db_initializer import COMPANY_JSON_PATH

QUERY = "https://www.alphavantage.co/query?"
FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"
OUTPUT_SIZE = "compact"
API_KEY = "AOTR8MTUM9ZQ10R4"

TIME_SERIES_DAILY = "Time Series (Daily)"


def cons_url(symbol):
    url = f"{QUERY}function={FUNCTION}&symbol={symbol}&outputsize={OUTPUT_SIZE}&apikey={API_KEY}"
    return url


def download_one_stock(symbol):
    url = cons_url(symbol)
    response = requests.get(url)
    data = response.json()
    return data[TIME_SERIES_DAILY]


def insert_stock(symbol, time_series):
    handler = DBHandler()
    for date, data in time_series.items():
        open_p = data["1. open"]
        high = data["2. high"]
        low = data["3. low"]
        close = data["4. close"]
        adjusted = data["5. adjusted close"]
        volume = data["6. volume"]
        dividend = data["7. dividend amount"]
        split = data["8. split coefficient"]
        handler.insert_price(symbol, date, open_p, high, low, close, adjusted, volume, dividend, split)


def update_all_stock():
    all_comp = json.load(open(COMPANY_JSON_PATH, "r"))
    download_failures = []
    # for i in range(0, 10906):
    for i in range(280, 320):
        key = str(i)
        symbol = all_comp[key]["ticker"]
        print("Start updating %s. %s..." % (key, symbol))
        try:
            time_series = download_one_stock(symbol)
        except Exception as result:
            print(result)
            download_failures.append(symbol)
        else:
            insert_stock(symbol, time_series)
            print("%s. %s successfully updated." % (key, symbol))
            print()
    if len(download_failures) > 0:
        print("Download finished, failure:", download_failures)


if __name__ == "__main__":
    update_all_stock()
