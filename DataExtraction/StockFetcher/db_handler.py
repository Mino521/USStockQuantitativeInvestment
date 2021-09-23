from conn_util import *


class DBHandler:

    def __init__(self):
        self.conn = my_connector()
        self.my_cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def insert_company(self, cik, ticker, title):
        self.my_cursor.execute(
            "INSERT INTO Company (cik, symbol, title) "
            "VALUES (%s, %s, %s)",
            (cik, ticker, title)
        )
        self.conn.commit()

    def insert_price(self, symbol, date, open_p, high, low, close, adjusted, volume, dividend, split):
        if self.exists_company_date_price(symbol, date) is False:
            try:
                self.my_cursor.execute(
                    "INSERT INTO Price (symbol, date, open, high, low, close, adjusted, volume, dividend, split) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (symbol, date, open_p, high, low, close, adjusted, volume, dividend, split)
                )
                self.conn.commit()
            except Exception as result:
                print(result)
                print(symbol, date, open_p, high, low, close, adjusted, volume, dividend, split)

    def exists_company(self, symbol):
        self.my_cursor.execute(
            "SELECT * FROM Company where symbol=%s", (symbol, )
        )
        result = self.my_cursor.fetchall()
        return len(result) > 0

    def exists_company_price(self, symbol):
        self.my_cursor.execute(
            "SELECT * FROM Price where symbol=%s", (symbol,)
        )
        result = self.my_cursor.fetchall()
        return len(result) > 0

    def exists_company_date_price(self, symbol, date):
        self.my_cursor.execute(
            "SELECT * FROM Price where symbol=%s and date=%s", (symbol, date)
        )
        result = self.my_cursor.fetchall()
        return len(result) > 0

    def get_all_company(self):
        self.my_cursor.execute(
            "SELECT symbol FROM Company"
        )
        result = self.my_cursor.fetchall()
        companies = []
        for tup in result:
            companies.append(tup[0])
        return companies
