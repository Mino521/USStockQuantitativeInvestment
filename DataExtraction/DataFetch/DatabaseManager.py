import sqlite3
import pandas as pd

def create_latest_content_table(c):
    #'insert into latest_content (CIK, Ticker, ReportDate, Year, totalCurrAssets, totalCurrLiabs, ' \
    #                 'longTermDebt, Income, Total_Share, Quarter, dividend, bookValue, sharePrice)
    c.execute("CREATE TABLE IF NOT EXISTS latest_content (CIK INT, Ticker VARCHAR(20) Primary Key, ReportDate TEXT, Year INT, totalCurrAssets REAL, totalCurrLiabs REAL, longTermDebt REAL,"
                                      "Income REAL, Total_Share REAL, Quarter INT, dividend INT, bookValue Real, sharePrice Real)")

def create_test_result_table(c):
    c.execute("Create table if not exists test_result (CIK int, "
              "Ticker varchar(20) Primary Key, Test_1 int, Test_2 int, Test_3 int, Test_4 int, Test_5 int, Test_6 int)")

def create_archive_content_table(c):
    c.execute(
        "CREATE TABLE IF NOT EXISTS archive_content (ID INTEGER Primary Key, CIK INT, Year INT, EarningsPerShare REAL)")
    print('Down!')


def create_comp_meta_table(c):
    c.execute('''CREATE TABLE IF NOT EXISTS COMP_META
                         (SIC INT, CIK INT, Ticker VARCHAR(20) PRIMARY KEY, Company VARCHAR(100), State_Country VARCHAR(20), Office VARCHAR(50))''')

def create_sic_infor_table(c):
    c.execute('''CREATE TABLE SIC_INFOR
                     (SIC INT PRIMARY KEY, Office VARCHAR(50), Industry_Title VARCHAR(50))''')

def drop_table(name, c):
    c.execute("DROP TABLE IF EXISTS " + name)
    print('done!')


def create_ticker_table(conn, c):
    df = pd.read_json('company_tickers.json')
    df = df.transpose()
    c.execute('CREATE TABLE Ticker_Infor (cik_str, ticker, title)')
    conn.commit()
    df.to_sql('Ticker_Infor', conn, if_exists='replace', index=False)

def main():
    conn = sqlite3.connect('secDB.db')
    c = conn.cursor()
    create_latest_content_table(c)
    create_test_result_table(c)
    create_archive_content_table(c)
    create_comp_meta_table(c)
    create_sic_infor_table(c)
    create_ticker_table(conn, c)
    conn.close()

if __name__=='__main__':
    main()
