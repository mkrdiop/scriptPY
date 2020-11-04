#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:13:33 2019

@author: makhtardiop
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

data=pd.read_csv('routes.csv')
#driver = webdriver.Chrome()
driver.get("https://www.advancedconverter.com/map-tools/find-altitude-by-coordinates")

for i in range(len(data)):
        lat = driver.find_element_by_id("lat")
        lat.clear()
        lat.send_keys(data.ix[i]['lat'])
        lon = driver.find_element_by_id("lon")
        lon.clear()
        lon.send_keys(data.ix[i]['lon'])
        button = driver.find_element_by_id("insertPoint")
        button.click()
        altitude=driver.find_element_by_id("outputDiv")
        time.sleep(20)
        data.loc[i]['altitude']=altitude
        print(data.ix[i])
        
        
        
