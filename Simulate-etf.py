#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:39:12 2019

@author: makhtardiop
"""
import pandas as pd

weight=pd.read_csv('spy_holdings.csv')
constituents=pd.read_csv('spy-set.csv') 
spy=pd.read_csv('/Users/makhtardiop/spy/SPY.csv')
taille=len(constituents)
portfolio=pd.DataFrame(index=range(len(constituents)-1)) 
pnl=pd.DataFrame(index=range(len(constituents)-1), columns=['replicated', 'SPY']) 
stocks=weight.columns


for stock in stocks[1:]:
    for f in range (len(portfolio)-1):
        portfolio[stock]=float(weight[stock][1])*constituents[stock].diff()[1:]
    print(portfolio.head())


portfolio.to_csv('portfolio.csv')

for i in range (1, len(portfolio)):

    pnl.loc[i]['replicated']=float(portfolio.loc[i].sum())
    print (pnl.loc[i])

    
    
#spy-pnl=100 * (spy['open'][1:]-spy['open'][:taille-1])

pnl['SPY']= spy['open'].diff()[1:]
pnl.to_csv('replicated-spy.csv')