from DatabaseUtil import *
from RequestData import *
import constants
import json

config = {
    'host': 'cadb.cc0uav02d2tx.ap-southeast-2.rds.amazonaws.com',
    'user': 'admin',
    'password': 'HtIONyOLbioppFsbdSsG',
    'port': 3306
}
DB_NAME = 'company_analysis_data'


def init():

    create_database(cursor, DB_NAME)
    create_table(cursor, DB_NAME, constants.Tables.TABLES)


if __name__ == '__main__':

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # create database and tables
    init()

    with open("company_tickers.json", 'r') as load_f:
        companies = json.load(load_f)
        for key, value in companies.items():
            ticker = value['ticker']
            for function_name in ["OVERVIEW", "EARNINGS", "INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"]:
                code = query_data(function_name, ticker, conn, cursor)
            if code == 1:
                print("Done with " + ticker)
            else:
                print("{} data missing!".format(ticker))

    cursor.close()
    conn.close()
