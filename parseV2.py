#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 17:26:54 2020

@author: makhtardiop
"""

from iex_parser import Parser, TOPS_1_6
import pandas as pd
TOPS_SAMPLE_DATA_FILE = 'data_feeds_20191226_20191226_IEXTP1_TOPS1.6.pcap.gz'

def insert(data, message, i, stock,file):
    data.iloc[i]['time']=message['timestamp']
    data.iloc[i]['symbol']=message['symbol']
    data.iloc[i]['bid_size']=message['bid_size']
    data.iloc[i]['bid_price']=message['bid_price']
    data.iloc[i]['ask_size']=message['ask_size']
    data.iloc[i]['ask_price']=message['ask_price']
    data.to_csv('IEXDATA/KOPEP/%s-quotes-%s.csv' % (stock,file))
    
"""
'type': 'quote_update', 'flags': 0, 'timestamp': 
    datetime.datetime(2019, 12, 26, 20, 58, 7, 55821, tzinfo=datetime.timezone.utc), 'symbol': b'KO', 'bid_size': 200, 'bid_price': Decimal('54.97'), 'ask_size': 100, 'ask_price': Decimal('55')}
"""

data=pd.DataFrame(index=range(10000), columns=['time','symbol','bid_size','bid_price','ask_size','ask_price'])
data2=pd.DataFrame(index=range(10000), columns=['time','symbol','bid_size','bid_price','ask_size','ask_price'])
i=0
p=0
file1=1
file2=1
with Parser(TOPS_SAMPLE_DATA_FILE, TOPS_1_6) as reader:
    for message in reader:
        #print (message['type'])
        if message['type'] =='quote_update' :
            if message['symbol'] == b'KO' :
                try:
                    insert(data, message, i, 'KO',file1)
                except IndexError:
                    file1=file1+1
                    data=pd.DataFrame(index=range(10000), columns=['time','symbol','bid_size','bid_price','ask_size','ask_price'])
                    i=0
                    insert(data, message, i, 'KO', file1)
                    
                i=i+1
                print(message)
            else :
                if message['symbol'] == b'PEP' :
                    try:
                        insert(data2, message, p, 'PEP',file2)
                    except IndexError:
                        file2=file2+1
                        data2=pd.DataFrame(index=range(10000), columns=['time','symbol','bid_size','bid_price','ask_size','ask_price'])
                        p=0
                        insert(data2, message, p, 'PEP', file2)
                    p=p+1
                    print(message)