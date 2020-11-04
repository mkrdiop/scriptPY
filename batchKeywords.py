#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 16:09:02 2019

@author: makhtardiop
"""
import os
import pandas as pd
import sys

villes = pd.read_csv('dataFrench.csv', encoding = "ISO-8859-1")
data=pd.DataFrame(index=range(len(villes)), columns=['ville','page','url'])

platform=sys.argv[1]
toreplace=sys.argv[2]
for i in range(len(villes)):
    town=villes.loc[i]['name']
    keyword='%s %s' % (platform, town)
    print (keyword)
    town=town.replace('\'','-')
    filename='Livreur-%s-%s.html' % (platform, town.replace(' ','-'))
    url='http://www.adsmuze.com/france/foodora/%s' % filename
    script="python /Users/makhtardiop/testpage.py %s %s %s" % (platform, town.replace(' ','-'), toreplace)
    os.system(script)
    
    
    data.loc[i,'page']=filename
    data.loc[i,'url']=url
    data.loc[i,'ville']=villes.ix[i]['name']
    data.to_csv('page%sFrance.csv' % platform )