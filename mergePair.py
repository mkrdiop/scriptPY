#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:36:37 2020

@author: makhtardiop
"""
import pandas as pd
import sys


stock1= sys.argv[1]
stock2= sys.argv[2]

ko=pd.read_csv('IEXDATA/%s-intraday.csv' % stock1)
pep=pd.read_csv('IEXDATA/%s-intraday.csv' % stock2)
pep=pep.dropna()
ko=ko.dropna()
ko=ko.astype({'time': 'int64'})
ko=ko.set_index('time')
pep=pep.astype({'time': 'int64'})
pep=pep.set_index('time')

print (pep.head())
#timeset=set(ko.time)
#timeset.add(e for e in pep.time)
#print (timeset)
#numbers = [ s for s in timeset ]
#numbers=numbers.sort()
dataset=pd.DataFrame(index=range(10), columns=['ko-vol','pep_vol','ko-iso','pep_iso'])
#numbers = [ 1 , 3 , 4 , 2 ] # Sorting list of Integers in ascending. 
print (dataset.index)
#data=ko.merge(pep, left_index=True, right_index=True)
#data=ko.merge(pep, left_on='size', right_on='size')

#data = pd.merge(ko,pep).dropna().reset_index()

#print (ko.join(pep.set_index('time'), on='time').dropna())
data=pd.merge(ko, pep, how='outer', left_index=True, right_index=True, suffixes=('_x', '_y'))
data.to_csv('IEXDATA/%s-%s-merged.csv' % (stock1,stock2))
print (data.head())
for index in dataset.index:
    print ("looking for data for index %s" % index)
    koline=ko.loc[ko['time'] == index]
    print(koline.size)
    dataset.loc[index]['ko_vol']=koline.size
    dataset.loc[index]['ko_iso']=koline.iso
    
    pepline=pep.loc[pep['time'] == index]
    dataset.loc[index]['pep_vol']=pepline.size
    dataset.loc[index]['pep_iso']=pepline.iso
    
    print (dataset.loc[index])
