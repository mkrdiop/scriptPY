#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 07:11:34 2020

@author: makhtardiop
"""

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
    data.iloc[i]['size']=message['size']
    data.iloc[i]['price']=message['price']
    data.iloc[i]['flag']=message['flags']
    data.iloc[i]['trade_id']=message['trade_id']
    if message['flags']==128:
        data.iloc[i]['iso']=1
    else:
        data.iloc[i]['iso']=0
        print ('not iso')
        if message['flags']==8:
            data.iloc[i]['crossed']=1
        else:
            data.iloc[i]['crossed']=0
            
        
        
    data.to_csv('IEXDATA/KOPEP/%s-trades-%s.csv' % (stock,file))
    
"""
'type': 'quote_update', 'flags': 0, 'timestamp': 
    datetime.datetime(2019, 12, 26, 20, 58, 7, 55821, tzinfo=datetime.timezone.utc), 'symbol': b'KO', 'bid_size': 200, 'bid_price': Decimal('54.97'), 'ask_size': 100, 'ask_price': Decimal('55')}
"""

data=pd.DataFrame(index=range(10000), columns=['time','symbol','flag','iso','crossed','size','price','trade_id'])
data2=pd.DataFrame(index=range(10000), columns=['time','symbol','flag','iso','crossed','size','price','trade_id'])
i=0
p=0
file1=1
file2=1
with Parser(TOPS_SAMPLE_DATA_FILE, TOPS_1_6) as reader:
    for message in reader:
        #print (message['type'])
        if message['type'] =='trade_report' :
            if message['symbol'] == b'SPY' :
                try:
                    insert(data, message, i, 'SPY',file1)
                except IndexError:
                    file1=file1+1
                    data=pd.DataFrame(index=range(10000), columns=['time','symbol','flag','size','price','trade_id'])
                    i=0
                    insert(data, message, i, 'SPY', file1)
                    
                i=i+1
                print(message)
            else :
                if message['symbol'] == b'TLT' :
                    try:
                        insert(data2, message, p, 'TLT',file2)
                    except IndexError:
                        file2=file2+1
                        data2=pd.DataFrame(index=range(10000), columns=['time','symbol','flag','size','price','trade_id'])
                        p=0
                        insert(data2, message, p, 'TLT', file2)
                    p=p+1
                    print(message)