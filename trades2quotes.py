#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:23:54 2020

@author: makhtardiop
"""
import pandas as pd


data=pd.read_csv('IEXDATA/KOPEP/KO-trades-1.csv')
data2=pd.read_csv('IEXDATA/KOPEP/KO-quotes-1.csv')

market=pd.DataFrame(index=range(len(data)+len(data2)), columns=['time', 'symbol', 'flag', 'iso', 'size',
        'trade_id','price', 'bid_size', 'bid_price', 'ask_size','ask_price'])
p=0
k=0
for i in range (len(data)):
    print ("hah ah ah")
    if data.loc[i]['time']< data2.loc[p]['time']:
        market.iloc[k]['time']=data.loc[i]['time']
        market.iloc[k]['symbol']=data.loc[i]['symbol']
        market.iloc[k]['flag']=data.loc[i]['flag']
        market.iloc[k]['iso']=data.loc[i]['iso']
        market.iloc[k]['size']=data.loc[i]['size']
        market.iloc[k]['price']=data.loc[i]['price']
        market.iloc[k]['trade_id']=data.loc[i]['trade_id']
        print (market.loc[k])
        k=k+1
       
        
    else:
        print ("not not not")
        while data.loc[i]['time']>= data2.loc[p]['time'] :
            print ("boucle boucle boucle")
            market.iloc[k]['time']=data2.loc[p]['time']
            market.iloc[k]['symbol']=data2.loc[p]['symbol']
            market.iloc[k]['bid_size']=data2.loc[p]['bid_size']
            market.iloc[k]['bid_price']=data2.loc[p]['bid_price']
            market.iloc[k]['ask_size']=data2.loc[p]['ask_size']
            market.iloc[k]['ask_price']=data2.loc[p]['ask_price']
            print (market.loc[k])
            p=p+1
            k=k+1
    market.to_csv('IEXDATA/KOPEP/KO-trades2quotes-1.csv')
    