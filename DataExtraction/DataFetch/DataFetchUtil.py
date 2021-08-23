import pandas as pd
from datetime import datetime
import os
import time
import random
import urllib3
import certifi
import DataSaveUtil


class DataFetcher:
    def __init__(self):
        df = pd.read_json('company_tickers.json')
        df = df.transpose()
        df['cik_str'] = df['cik_str'].astype('int32')
        self.df = df
        self.office = {'Office of Life Sciences', 'Office of Manufacturing', 'Office of Technology',
                       'Office of Trade & Services'}
        self.hdr = {'User-Agent': 'justin@juke.net.au'}
        self.http = urllib3.PoolManager(
            cert_reqs="CERT_REQUIRED",
            ca_certs=certifi.where())
        self.active_cik = self.get_cik_ticker_dic()
        self.sic_filter = self.get_sic_dictionary()

    def start_download(self, conn, set_sleep, index_folder='report_index'):
        for year in range(self, datetime.today().year):
            for i in range(1, 5):
                t_f = os.path.join(index_folder, str(year) + 'q' + str(i), 'sub.txt')
                if os.path.exists(t_f):
                    self.download_report(year=year, index_file=t_f, active_cik=self.active_cik,
                                         sic_filter=self.sic_filter, conn=conn, set_sleep=set_sleep)
                else:
                    print('Please download the latest quarter report:' + str(year) + 'q' + str(i))
            print('Done for year' + str(year))

    def download_report(self, year, index_file, active_cik, sic_filter, conn, US_ONLY=True, FY_ONLY=True, set_sleep=True):
        df = pd.read_csv(index_file, delimiter="\t")
        if not os.path.exists('data/' + str(year)):
            os.mkdir('data/' + str(year))

        if FY_ONLY:
            df = df[df['fp'] == 'FY']

        if US_ONLY:
            df = df[df['countryma'] == 'US']

        print(len(df.index))
        for i, r in df.iterrows():
            cik = int(r['cik'])
            if cik in active_cik and sic_filter[int(r['sic'])] in self.office and not os.path.exists(
                    'data/' + str(year) + '/' + str(cik) + '.xml'):
                for ticker in active_cik[cik]:
                    DataSaveUtil.insert_comp_infor_table(conn, int(r['sic']), int(r['cik']), ticker, r['name'],
                                                         r['stprba'],
                                                         sic_filter[int(r['sic'])])
                url = 'http://www.sec.gov/Archives/edgar/data/' + str(r['cik']) + '/' + r['adsh'].replace('-',
                                                                                                          '') + '/' + \
                      r['instance']
                req = self.http.request('GET', url, headers=self.hdr)
                content = req.data
                open('data/' + str(year) + '/' + str(r['cik']) + '.xml', 'wb').write(content)
                for ticker in active_cik[cik]:
                    DataSaveUtil.insert_comp_infor_table(conn, int(r['sic']), cik, ticker, r['name'], r['stprba'],
                                                         sic_filter[int(r['sic'])])

        if set_sleep:
            time.sleep(random.uniform(0.5, 1.0))

    def get_sic_dictionary(self):
        df_sic = pd.read_csv('SIC_infor.csv')
        sic_list = df_sic[['SIC Code', 'Office']].values
        return dict(sic_list)

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
