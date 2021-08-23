
import logging
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool
import os 
from urllib.request import urlopen, Request
import xml.etree.ElementTree as et
import logging
from bs4 import BeautifulSoup
from datetime import datetime, date
import urllib3
import time
import random
import YahooDownloader as yd
import certifi

curr_year = date.today().year
http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where())
hdr = {'User-Agent': 'justin@juke.net.au'}
#an email address
def set_agent(agent):
    hdr =  {'User-Agent': agent}

office = {'Office of Life Sciences', 'Office of Manufacturing', 'Office of Technology', 'Office of Trade & Services'}

def get_sic_dictionary():
    df_sic = pd.read_csv('SIC_infor.csv')
    sic_list = df_sic[['SIC Code', 'Office']].values
    return dict(sic_list)

class TickerInfor:
    def __init__(self):
        df = pd.read_json('company_tickers.json')
        df = df.transpose()
        df['cik_str'] = df['cik_str'].astype('int32')
        self.df = df
        
    def get_ticker_cik_dic(self):
        return dict(self.df[['ticker', 'cik_str']].values)
    
    def get_cik_ticker_dic(self):
        dic = {}
        for i, r in self.df.iterrows():
            if r['cik_str'] in dic:
                dic[r['cik_str']].add(r['ticker'])
            else:
                dic[r['cik_str']] = {r['ticker']}
                
        return dic

def insert_comp_infor_table(conn, sic, cik, ticker, comp_name, state, office):
    sql = 'insert or ignore into comp_meta (sic, cik, ticker, company,' \
          ' state_country,office) values (?,?,?,?,?,?);'
    try:
        project = [sic, cik, ticker, comp_name, state, office]
        conn.execute(sql, project)
        conn.commit()
    except Exception as e:
        print(e)
        
#read the predownloaded index file, saved as sub.txt
def download_report(year, index_file, active_cik, sic_filter, conn, US_ONLY = True, FY_ONLY = True, set_sleep = True):
    
    # read csv file 
    df = pd.read_csv(index_file, delimiter = "\t")
    if not os.path.exists('data/' + str(year)):
        os.mkdir('data/' + str(year))
    
    if FY_ONLY:
        df = df[df['fp'] == 'FY']
    #we only consider american companies
    
    if US_ONLY:
        df = df[df['countryma'] == 'US']
        
    print(len(df.index))
    for i, r in df.iterrows():
        cik = int(r['cik'])
        if cik in active_cik and sic_filter[int(r['sic'])] in office and not os.path.exists('data/' + str(year) +'/'+str(cik)+'.xml'):
            for ticker in active_cik[cik]:
                insert_comp_infor_table(conn, int(r['sic']), int(r['cik']),ticker, r['name'], r['stprba'],sic_filter[int(r['sic'])])
            url = 'http://www.sec.gov/Archives/edgar/data/' + str(r['cik']) + '/' + r['adsh'].replace('-', '') + '/' + r['instance']
            req = http.request('GET', url, headers =  hdr)
            content = req.data
            open('data/' + str(year) +'/'+str(r['cik'])+'.xml', 'wb').write(content)
            for ticker in active_cik[cik]:
                insert_comp_infor_table(conn, int(r['sic']), cik, ticker, r['name'], r['stprba'],sic_filter[int(r['sic'])])
    
    if set_sleep:            
        time.sleep(random.uniform(0.5,1.0))
    
                
def download_and_extract_archive_report(year, index_file, active_cik, sic_filter, conn, US_ONLY = True, FY_ONLY = True, update = False):
    df_o = pd.read_csv(index_file, delimiter = "\t")
    #result = []
    if not os.path.exists('data/' + str(year)):
        os.mkdir('data/' + str(year))
        print('make a new folder:' + 'data/' + str(year))

    df_o = df_o.dropna(subset=['sic', 'cik'])
    
    if US_ONLY:
        df_o = df_o[df_o['countryma'] == 'US']
        
    if FY_ONLY:
        df = df_o[df_o['fp'] == 'FY']
    else:
        df = df_o
    #we only consider american companies
    #uniq_ticker = {}
    
    count = 0 
    print("start to download records from index: " + index_file)
    number = 0
    for i, r in df.iterrows():
            cik = int(r['cik'])
            if cik in active_cik and sic_filter[int(r['sic'])] in office:
                url = 'http://www.sec.gov/Archives/edgar/data/' + str(r['cik']) + '/' + r['adsh'].replace('-', '') + '/' + r['instance']
                req = http.request('GET', url, headers =  hdr)
                content = req.data
                income, f_year = parse_archive_data(content.decode('utf-8'))
                save_to_db(int(r['cik']), f_year, income, conn)
                #result.append({'CIK': int(r['cik']), 'Year': f_year, 'EaringPerShare':income})
                number += 1
                for ticker in active_cik[cik]:
                    insert_comp_infor_table(conn, int(r['sic']), cik, ticker, r['name'], r['stprba'],sic_filter[int(r['sic'])])
                    #print(ticker)
            count += 1   
            if count % 100 == 0:
                p = count/len(df)
                print("file:" + index_file + "\t Progress: {:.4f}".format(p))
            
    print('download total: ' + str(number) + ' report from' + index_file)
    
    
    if update:
        print('start to donwload yahoo finance.')
        c = 0
        num = 0
        for i, r in df_o.iterrows():
            cik = int(r['cik'])
            if cik in active_cik and sic_filter[int(r['sic'])] in office:
                for ticker in active_cik[cik]:
                    insert_comp_infor_table(conn, int(r['sic']), cik, ticker, r['name'], r['stprba'],sic_filter[int(r['sic'])])
                    yd.download_yahoo_f(ticker, cik, conn, False)
                    num += 1
            c += 1    
            if c % 20 == 0:
                print("Progress: {:.4f}".format(c/len(df_o)))
        
        print('update total: ' + str(number) + ' reports - yahoo finance')
                          

def extract_from_downloaded_files(folder, conn):
    files = os.listdir(folder)
    #result = []
    for a_f in files:
        income, year = parse_archive_data(os.path.join(folder, a_f))
        cik = int(a_f.replace('.xml', ''))
        save_to_db(cik, year, income, conn)

def convert_time(string):
    try:
        #'Jun 1 2005  1:33PM'
        return datetime.strptime(string, "%Y-%m-%d")
    except Exception as e:
        return None
    
        
def parse_archive_data(content): 
    if content.endswith('xml'):
        soup = BeautifulSoup(open(content, 'r'), 'lxml')
    else:
        soup = BeautifulSoup(content, 'lxml')
        
    tag_list = soup.find_all()
    income_time = share_time = div_time = datetime(1989, 1, 1) 
    income = share = dividend = 0
    for tag in tag_list:
        if tag.name == 'us-gaap:earningspersharebasic' or tag.name == 'us-gaap:earningspersharebasicanddiluted' or tag.name == 'us-gaap:earningspersharediluted':
            context, prefix = find_tag(soup, tag)
            if context:
                if prefix:
                    context = context.find(prefix + ':enddate')
                else:
                    context = context.find('enddate')
                
                if context:
                    
                    tm = convert_time(context.text.strip())
                    if tm and income_time < tm:
                        income_time = tm
                        if tag.text:
                            income = float(tag.text)
    return  income, income_time.year


    
    
def find_tag(soup, tag):
    context = soup.find('xbrli:context', {'id':str(tag['contextref'])})
    if context:
        return context, 'xbrli'
    else:
        context = soup.find('context', {'id':str(tag['contextref'])})
        return context, None
            

#insert data into the latest_content table
def save_to_db(cik, year, income, conn):
    try:
        sql = 'insert or ignore into archive_content (ID, CIK, Year, EarningsPerShare) VALUES (?,?,?,?);'
        project = [int(str(cik) + str(year)), cik, year, income]
        conn.execute(sql, project)
        conn.commit()
    except Exception as e:
        logging.warning(e)