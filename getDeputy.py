#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:15:28 2019

@author: makhtardiop
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

data = pd.read_csv('liste-deputes.csv')
rich_data = pd.DataFrame(index=range(0,1800), columns = [ 'nom', 'groupement', 'departement', 'legislature', 'link','image'])
driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path = '/Users/makhtardiop/chrome/')
f=0
for i in range(372,len(data)):
    driver.get(data.iloc[i]['Nom_link'])
    time.sleep(20)
    rich_data.iloc[i]['link']=data.iloc[i]['Nom_link']
    rich_data.iloc[i]['nom']=data.iloc[i]['Nom']
    print (data.iloc[i]['Nom'])
    image=driver.find_element_by_css_selector('div.deputes-image.sycomore-image')
    img=image.find_element_by_tag_name('a')
    img_link=img.get_attribute('href')
    print (img_link)
    elems = driver.find_elements_by_css_selector("dl.deputes-liste-attributs.sycomore")
    
    for elem in elems:
        rich_data.iloc[f]['link']=data.iloc[i]['Nom_link']
        rich_data.iloc[f]['image']=img_link
        rich_data.iloc[f]['nom']=data.iloc[i]['Nom']
        get_dds = driver.find_elements_by_tag_name('dd')
        rich_data.iloc[f]['legislature']=get_dds[2].text
        rich_data.iloc[f]['departement']=get_dds[4].text
        rich_data.iloc[f]['groupement']=get_dds[5].text
        #print (rich_data.iloc[i]['groupement'])
    print (rich_data.iloc[f])
    f=f+1
        
        
    rich_data.to_csv('liste-groupe-depute2.csv')
    
            
        
    
    
    
"""   
    
    
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()

"""