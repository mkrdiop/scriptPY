#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:26:09 2019

@author: makhtardiop
"""

import iexfinance
from iexfinance.stocks import Stock
import pandas as pd

def iex_charts(symbols):
    partlen = 99
    result = {}
    for i in range(0, len(symbols), partlen):
        charts = Stock(symbols[i:i+partlen]).get_chart(range='1m') #iexfinance.Stock(symbols[i:i+partlen]).get_chart(range='1m')
        if type(charts) == list:
            charts = {symbols[i]: charts}
        for symbol, data in charts.items():
            df = pd.DataFrame(data)
            df.date = pd.to_datetime(df.date)
            df.set_index('date', inplace=True)
            df.index.names = ['epoch']
            df.index = df.index.tz_localize('America/New_York')
            result[symbol] = df
    return result

def get_closes(constituents):
    symbols =list(constituents) # list(constituents.columns)
    charts = iex_charts(symbols)
    dataset=pd.DataFrame({symbol: df.close for symbol, df in charts.items()}) 
    dataset.to_csv('spy-history.csv')
    print (dataset.head())
    return pd.DataFrame({symbol: df.close for symbol, df in charts.items()})  

data=pd.read_csv('spy_holdings.csv')
constituents=data.columns

get_closes(constituents[1:])
