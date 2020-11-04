#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:03:08 2019

@author: makhtardiop
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

data = pd.read_csv('liste-groupe-depute.csv')
liste_groupe=set(data['groupement'])
groupes=pd.DataFrame(index=range(0,len(liste_groupe)), columns=['group_name'])
deputies(index=range(0,len(set(data['nom']))), columns=['nom', 'groupement', 'depart', 'legislature', 'link','nbr_mandat','change'])

# Building Group lists
f=0
for groupe in liste_groupe:
    groupe.iloc[f]['group_name']=groupe
    f=f+1
groupes.to_csv('liste_groupe.csv')
    
rich_data = pd.DataFrame(index=range(0,1800), columns = [ 'nom', 'groupement', 'depart', 'legislature', 'link','nbr_mandat',''])


# computing number of mandat

for name in data['nom']:
    print(name)
    filtered_data = data[data.nom == name]
    nbr_mandat=len(set(filtered_data['legislature']))
    print(nbr_mandat)
    


for i in range(len(data)):

driver = webdriver.Chrome()

for i in range(len(data)):
    driver.get(data.iloc[i]['Nom_link'])
    rich_data.iloc[i]['link']=data.iloc[i]['Nom_link']
    rich_data.iloc[i]['nom']=data.iloc[i]['Nom']
    print (data.iloc[i]['Nom'])
    elems = driver.find_elements_by_css_selector("dl.deputes-liste-attributs.sycomore")
    time.sleep(20)
    for elem in elems:
        rich_data.iloc[i]['link']=data.iloc[i]['Nom_link']
        rich_data.iloc[i]['nom']=data.iloc[i]['Nom']
        get_dds = driver.find_element_by_tag_name('dd')
        rich_data.iloc[i]['legislature']=get_dds[1].text
        rich_data.iloc[i]['depart']=get_dds[3].text
        rich_data.iloc[i]['groupement']=get_dds[4].text
        print (rich_data.iloc[i]['groupement'])
    rich_data.to_csv('liste-groupe-depute.csv')
        