#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 06:14:51 2020

@author: makhtardiop
"""
from IEXTools import Parser, messages
import pandas as pd
import sys

"""
with Parser(r'iex.pcap') as iex_messages:
    for message in iex_messages:
        #do_something(message)
        print (message.symbol)
        
"""
stock= sys.argv[1]
dataset=pd.DataFrame(index=range(20754), columns=['time','ticker','size','totalSize','iso','totalIso','isoSize'])
p = Parser(r'iex.pcap')
allowed = [messages.TradeReport]
size=0
trades=0
iso=0
iso_volume=0
i=0
while True :

    data=p.get_next_message(allowed)
    if data.symbol==stock:
        size =data.size+size
        trades=trades+1
        dataset.iloc[i]['iso']=0
        if data.flags==128:
            iso=iso+1
            iso_volume=iso_volume+data.size
            dataset.iloc[i]['sizeIso']=iso_volume+data.size
            dataset.iloc[i]['iso']=1
            dataset.iloc[i]['totalIso']=iso
            
        else :
            dataset.iloc[i]['totalIso']=0
            dataset.iloc[i]['isoSize']=0
            
        """   
        print("total trades= %s" % (trades))
        print("total volume= %s" % (size))
        print("total ISO orders= %s" % (iso))
        print("total ISO volume= %s" % (iso_volume))
        
        """
        dataset.iloc[i]['totalSize']=size
        dataset.iloc[i]['time']=data.timestamp
        dataset.iloc[i]['ticker']=stock
        dataset.iloc[i]['size']=data.size
        dataset.iloc[i]['price']=data.price_int
        
        dataset.to_csv('IEXDATA/%s-intraday.csv' % stock)
        print (dataset.ix[i])
        i=i+1
        
        print(data)