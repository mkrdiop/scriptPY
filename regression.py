#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:14:41 2019

@author: makhtardiop
"""

from sklearn.decomposition import PCA
import pandas as pd
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
from sklearn import linear_model


spy=pd.read_csv('/Users/makhtardiop/spy/SPY.csv')
portfolio=pd.read_csv('portfolio.csv')
target=pd.DataFrame(index=range(len(portfolio)), columns=['replicated', 'SPY']) 
weight=pd.read_csv('spy_holdings.csv')
stocks=weight.columns[1:]

print('filling nan data')
for stock in stocks:
    portfolio[stock]=portfolio[stock].fillna(portfolio[stock].mean())
    portfolio[stock]=portfolio[stock].replace('NaN', portfolio[stock].mean())


target['SPY']= spy['open'].diff()

target['SPY']=target['SPY'].fillna(target['SPY'].mean())

print('splitting traind and Test data')
x_train, x_test, y_train, y_test = train_test_split(portfolio[[stock for stock in stocks]], target['SPY'], test_size=0.25, random_state=0)

print (x_train.head())
print('Building the regresssion model')
lm = linear_model.LinearRegression()
model = lm.fit(x_train, y_train)
coef=lm.coef_
score = lm.score(x_test.values, y_test.values)

"""
logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)

score = logisticRegr.score(x_test, y_test)
"""
print(coef)
print(score)
poids=map(abs, coef)
total=0
for elem in poids:
    total=total+elem
    
print(total)
target['replicated']=lm.predict(portfolio[[stock for stock in stocks]].values)
target.to_csv('model.csv')

