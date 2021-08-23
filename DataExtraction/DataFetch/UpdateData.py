import sqlite3
import logging
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool
import os 
from urllib.request import urlopen, Request
import xml.etree.ElementTree as et
import string
import dateutil
import logging
from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime, date
import urllib3
import time
import random
import sys, getopt
import shutil
import utils
import yfinance as yf
import zipfile
import DataExtractor as ae



def main(args):
    ae.set_agent('justin@juke.net.au')
    download_only = False
    set_sleep = False
    extract_only = False
    download_and_extact = True
    init_project = True
    conn = sqlite3.connect('secDB.db')
            
    index_folder = 'report_index'
    sub_folders =  os.listdir(index_folder)
    flag = False
    for folder in sub_folders:
        if os.path.isdir(os.path.join(index_folder, folder)):
              flag = True
                         
    if not flag:
        files = os.listdir('report_index_zip')
        for f in files:
            with zipfile.ZipFile('report_index_zip/' + f, 'r') as zip_ref:
                fd = index_folder + '/' + f.replace('.zip', '')
                if not os.path.exists(fd):
                    os.mkdir(fd)
                zip_ref.extractall(fd)
    sub_folders =  os.listdir(index_folder)

                         
    print("load tickers information.....")
    ticker_infor = ae.TickerInfor()
    active_cik = ticker_infor.get_cik_ticker_dic()
    print("load company sic information.....")
    sic_filter = ae.get_sic_dictionary()
    today = datetime.today()
    if download_and_extact:
        print("start download and extract financial report...")
        for folder in sub_folders:
            t_f = os.path.join(index_folder, folder, 'sub.txt')
            if os.path.exists(t_f):
                ae.download_and_extract_archive_report(year = int(folder.split('q')[0]), index_file = t_f, active_cik = active_cik, sic_filter = sic_filter, conn = conn, update = True)
                print("finished downloading " + folder + " from US SEC.")

                shutil.move(os.path.join(index_folder, folder), 'report_index_old')
                shutil.move(os.path.join("report_index_zip", folder + ".zip"), 'report_index_old')
                print("moved the " + folder+ " to archive.")
                
            
    elif download_only:
        for year in range(2011, (today.year + 1)):
            r_list = []
            for i in range(1, 5):
                t_f = os.path.join(index_folder, str(year)+'q' + str(i), 'sub.txt')
                if os.path.exists(t_f):
                    ae.download_report(year = year, index_file = t_f, active_cik = active_cik, sic_filter = sic_filter, conn = conn, set_sleep = set_sleep)
                else:
                    print('Please download the latest quarter report:' + str(year)+'q' + str(i))
            print('Done for year' + str(year))
            
    elif extract_only:
        data_folder = 'data'
        year_folders = os.listdir(data_folder)
        for year_folder in year_folders:
            path = os.path.join(data_folder, year_folder)
            ae.extract_from_downloaded_files(path, conn)
            


if __name__ == '__main__':
    #args = sys.argv[1:]
    main([])