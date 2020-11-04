#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 01:39:13 2020

@author: makhtardiop
"""

import pandas as pd
from dateutil.parser import *
def t_microseconds(t):
    dt=t.total_seconds()
    return dt


data=pd.read_csv('IEXDATA/KOPEP/KO-trades-1.csv')
data=data.drop(['crossed'], axis=1)
data=data.dropna()
data['t']=data.loc[0:]['time'].apply(parse)
data['dt']=0.0
data['elapsed']=0.0
for i in range (1, len(data)):
    s=data.loc[i]['t']-data.loc[i-1]['t']
    s1=data.loc[i]['t']-data.loc[0]['t']
    data.loc[i,'dt']=float(s.total_seconds())
    data.loc[i,'elapsed']=float(s1.total_seconds())
    print (s.total_seconds())
    print (s)
    print (data.loc[i])
    data.to_csv('IEXDATA/KOPEP/richtime.csv')
 
    
"""
data['dt']=0
data.iloc[1:]['dt']=data.loc[2:]['t']-data.loc[1:]['t']
print (data['t'].head())
data.iloc[0]['dt']=0

data.iloc[1:]['dt']=data.iloc[1:]['dt'].apply(t_microseconds)
data.to_csv('IEXDATA/KOPEP/richtime.csv')


for i in range(len(data)):
    data.ix[1]['time']
    


float(s.total_seconds())

data.ix[1]['time']
time=data.ix[1]['time']
time
time.type
time.type()
type(time)
data.columns

now=parse(time)
now
time2=data.ix[2]['time']
now2=parse(time2)
now2-now1
now2-now
"""