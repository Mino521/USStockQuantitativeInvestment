import mysql.connector
import json
from conn_util import *
from db_handler import DBHandler

COMPANY_JSON_PATH = "../DataFetch/company_tickers.json"


def create_database():
    conn = my_connector(connect_database=False)
    my_cursor = conn.cursor()
    my_cursor.execute("DROP DATABASE IF EXISTS %s" % DATABASE)
    my_cursor.execute("CREATE DATABASE %s" % DATABASE)
    conn.close()


def create_tables():
    conn = my_connector()

    my_cursor = conn.cursor()
    my_cursor.execute(
        "DROP TABLE IF EXISTS Company"
    )
    my_cursor.execute(
        "DROP TABLE IF EXISTS Price"
    )
    my_cursor.execute(
        "CREATE TABLE Company("
        "No INT PRIMARY KEY AUTO_INCREMENT, "
        "symbol VARCHAR(50), "
        "cik VARCHAR(50), "
        "title VARCHAR(100)"
        ")"
    )
    my_cursor.execute(
        "CREATE TABLE Price("
        "symbol VARCHAR(50), "
        "date Date, "
        "open DOUBLE, "
        "high DOUBLE, "
        "low DOUBLE, "
        "close DOUBLE, "
        "adjusted DOUBLE, "
        "volume INT, "
        "dividend DOUBLE, "
        "split DOUBLE, "
        "PRIMARY KEY(symbol, date))"
    )
    conn.close()


def init_company():
    handler = DBHandler()
    all_comp = json.load(open(COMPANY_JSON_PATH, "r"))
    for key, value in all_comp.items():
        if int(key) % 2000 == 0:
            print(f'{int(key) // 100}% completed.')
        if handler.exists_company(value['ticker']) is False:
            handler.insert_company(value['cik_str'], value['ticker'], value['title'])


if __name__ == '__main__':
    print("Database Creating...")
    create_database()
    print("Database Created.\n")

    print("Tables Creating...")
    create_tables()
    print("Tables Created.\n")

    print("Company Info Initializing...")
    init_company()
    print("Company Info Initialized.")
