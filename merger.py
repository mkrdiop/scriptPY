#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:04:35 2020

@author: makhtardiop
"""

import pandas as pd

ko=pd.read_csv('IEXDATA/KO-intraday.csv')
pep=pd.read_csv('IEXDATA/PEP-intraday.csv')
pep=pep.dropna()
ko=ko.dropna()
ko=ko.astype({'time': 'int64'})
#ko=ko.set_index('time')
pep=pep.astype({'time': 'int64'})
#pep=pep.set_index('time')

dataset=pd.DataFrame(index=range((len(ko)+len(pep))), columns=['time','ko-vol','pep_vol','ko-iso','pep_iso'])

for i in range(len(ko)):
    dataset.iloc[i]['time']=ko.ix[i]['time']
    

for i in range(len(pep)):
    dataset.iloc[i]['time']=pep.ix[i]['time']
    
for i in range(len(ko)):
    dataset.iloc[i]['ko_vol']=ko.ix[i]['size']
    dataset.iloc[i]['ko_iso']=ko.ix[i]['iso']
    dataset.iloc[i]['time']=ko.ix[i]['time']
    
for i in range(len(pep)):
    print ("looking for data for index %s" % index)
    koline=ko.loc[ko['time'] == index]
    print(koline.size)
    dataset.loc[index]['ko_vol']=koline.size
    dataset.loc[index]['ko_iso']=koline.iso
    
    pepline=pep.loc[pep['time'] == index]
    dataset.loc[index]['pep_vol']=pepline.size
    dataset.loc[index]['pep_iso']=pepline.iso
    
    print (dataset.loc[index])