from bs4 import BeautifulSoup
from datetime import datetime
import os
from DataSaveUtil import save_to_db


def find_tag(soup, tag):
    context = soup.find('xbrli:context', {'id':str(tag['contextref'])})
    if context:
        return context, 'xbrli'
    else:
        context = soup.find('context', {'id':str(tag['contextref'])})
        return context, None


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
    return income, income_time.year

def extract_from_downloaded_files(folder, conn):
    files = os.listdir(folder)
    #result = []
    for a_f in files:
        income, year = parse_archive_data(os.path.join(folder, a_f))
        cik = int(a_f.replace('.xml', ''))
        save_to_db(cik, year, income, conn)