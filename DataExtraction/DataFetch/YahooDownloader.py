import sqlite3
import logging
import pandas as pd
import logging
from datetime import datetime, date

import utils
import yfinance as yf
curr_year = date.today().year
def update_data(result, c):
    

        sql = "update latest_content set ReportDate = ?, Year = ?, totalCurrAssets = ?," \
              " totalCurrLiabs = ?, longTermDebt = ?," \
              "Income = ?, Total_Share = ?, Quarter = ?, sharePrice = ?, dividend = ?, bookValue = ? where Ticker = ?;"

        # 'reportDate': report_date.to_pydatetime(), 'year': year,
        # 'quarter': quarter, 'totalCurrAssets': balance_values[0],
        # 'totalCurrLiabs': balance_values[1], 'longTermDebt': balance_values[2],
        # 'income': income, 'bookValue': bookValue, 'sharePrice': close_price,
        # 'totalShares': shares, 'dividend': div}
        project = [result['reportDate'], result['year'], result['totalCurrAssets'],
                   result['totalCurrLiabs'], result['longTermDebt'], result['income'],
                   result['totalShares'], result['quarter'], result['sharePrice'],
                   result['dividend'], result['bookValue'], result['ticker']]
        c.execute(sql, project)
        c.commit()
        
#this method use yfinance api, this one is faster
#ticker_cik is a tuple(ticker, cik)
def process_single_data(ticker_cik):
    try:
        comp = yf.Ticker(ticker_cik[0])

        hist_data = comp.history(period='20y')
        finance = comp.quarterly_financials
        balance = comp.quarterly_balance_sheet
        infor = comp.info

        

        # get the latest share price
        close_price = hist_data.tail(1)['Close'].values[0]

        # show balance sheet

        balance_trans = balance.transpose().sort_index(ascending=False)
        if 'Long Term Debt' in balance_trans.columns:
            balance_values = \
                balance_trans.head(1)[['Total Current Assets', 'Total Current Liabilities',
                                       'Long Term Debt']].values[0]
            longTermDebt = balance_values[2]
        else:
            balance_values = \
                balance_trans.head(1)[['Total Current Assets', 'Total Current Liabilities']].values[0]
            longTermDebt = 0

        report_date = balance_trans.index[0]
        year = report_date.year
        
        if len(hist_data) > 0:
            dividends = hist_data.groupby(hist_data.index.year)['Dividends'].sum()
            divs = dividends[dividends > 0].index.tolist()
            div = utils.check_continue_year(set(divs), curr_year - 20, curr_year)
        else:
            div = 0

        finance_trans = finance.transpose()
        income = finance_trans.sort_index(ascending=False).head(1)['Net Income'].values[0]

        bookValue = infor['bookValue']
        shares = infor['sharesOutstanding']
        last_fin_year = infor['lastFiscalYearEnd']
        days = report_date - datetime.fromtimestamp(last_fin_year)
        quarter = utils.check_quarter(days.days)
        result = {'ticker': ticker_cik[0], 'cik': ticker_cik[1],
                  'reportDate': report_date.to_pydatetime(), 'year': year,
                  'quarter': quarter, 'totalCurrAssets': balance_values[0],
                  'totalCurrLiabs': balance_values[1], 'longTermDebt': longTermDebt,
                  'income': income, 'bookValue': bookValue, 'sharePrice': close_price,
                  'totalShares': shares, 'dividend': div}
        #print(result)
        return result
    except Exception as e:
        logging.warning(str(ticker_cik[0]) +'\t'+str(e))

#insert data into the latest_content table
def fill_up_latest_content_table(result, conn):
            try:
                sql = 'insert into latest_content (CIK, Ticker, ReportDate, Year, totalCurrAssets, totalCurrLiabs, ' \
                      'longTermDebt, Income, Total_Share, Quarter, dividend, bookValue, sharePrice) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);'
                project = [result['cik'], result['ticker'], result['reportDate'],
                           result['year'], result['totalCurrAssets'],
                           result['totalCurrLiabs'], result['longTermDebt'], result['income'],
                           result['totalShares'], result['quarter'],
                           result['dividend'], result['bookValue'], result['sharePrice']]
                conn.execute(sql, project)
                conn.commit()
            except Exception as e:
                logging.warning(e)

def download_yahoo_f(ticker, cik, conn, update):
    sql = "select * from latest_content where ticker = '"+ticker+"';"
    df_r = pd.read_sql_query(sql, conn)
    if len(df_r) > 0:
        if update:
            rs = process_single_data((ticker, cik))
            if rs:
                update_data(rs, conn)
    else:
        rs = process_single_data((ticker, cik))
        if rs:
            fill_up_latest_content_table(rs, conn)
            
def main():
    conn = sqlite3.connect('secDB.db')
    sql = "select cik, ticker from comp_meta;"
    df_meta = pd.read_sql_query(sql, conn)
    print('Start to download data from Yahoo Finance ...')
    count = 0 
    for i, r in df_meta.iterrows():
        download_yahoo_f(r['Ticker'], r['CIK'], conn, False)
        count += 1
        if count % 20 == 0:
            print("Progress {:.2f}".format(count/len(df_meta)))
    print('Done!')

if __name__ == '__main__':
    main()
    
        
        
    