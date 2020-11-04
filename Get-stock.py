#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:57:41 2019

@author: makhtardiop
"""

from iexfinance.stocks import get_historical_data

import pandas as pd

i=0
data=pd.read_csv('spy_holdings.csv')
constituents=data.columns
dataset=pd.DataFrame(columns=['date'])
for stock in constituents[1:]:
   
    print ("getting data of %s" % stock)
    history=get_historical_data(stock, output_format='pandas')
    history.to_csv('/Users/makhtardiop/spy/%s.csv' % stock)
    dataset[stock]=history['open']
    
    if i==0:
        dataset['date']=history.index
        i=i+1
    dataset.to_csv('spy-set.csv')    
    print (dataset.head())