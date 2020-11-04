#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 12:49:30 2019

@author: makhtardiop
"""

from bs4 import BeautifulSoup as soup
import pandas as pd

#result = soup.find(id='websiteName')


villes = pd.read_csv('dataFrench.csv', encoding = "ISO-8859-1")
data=pd.DataFrame(index=range(len(villes)), columns=['ville','page','url'])
for i in range (len(villes)):
    file='/Users/makhtardiop/page1.html'
    html = open(file).read()
    soup = soup(html, 'lxml')
    platform='Foodora'
    keyword='%s %s' % (platform, villes.ix[i]['name'])
    print (keyword)
    filename='Livreur-%s-%s.html' % (platform, villes.ix[i]['name'].replace(' ','-'))
    url='http://www.adsmuse.com/%s' % filename
    
    """
    for elen in soup.find_all("div", {"class": "site-content-contain"}):
        print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora','Uber'))
        for a in elen.childGenerator():
            if a.string!= None:
                a.string.replace_with(a.string.replace('Foodora','Uber'))
      
    for elen in soup.find_all('div', {'class':'site-content'}):
        #print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
             
        #for a in elen.childGenerator():
            #if a.string!= None:
                #a.string.replace_with(a.string.replace('Foodora',keyword))
           
    for elen in soup.find_all('br'):
        #print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
             
    for elen in soup.find('h1'):
        #print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
        for a in elen.childGenerator():
            if a.string!= None:
                a.string.replace_with(a.string.replace('Foodora',keyword))
    
    """        
    for elen in soup.findAll('h1'):
        #print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
        
    
    for elen in soup.findAll('h2'):
        #print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
        
                
                
    for elen in soup.findAll('h3'):
        #print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
        
    
    for elen in soup.findAll('h4'):
        #print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
        
    
    for elen in soup.findAll('h5'):
        #print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
        
    
    for elen in soup.findAll('a'):
        #print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
        
    
    for elen in soup.findAll('figcaption'):
        print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
        
                
    for elen in soup.findAll('title'):
        print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
        
                
    for elen in soup.findAll('p'):
        print(elen.string)
        if elen.string!= None:
             elen.string.replace_with(elen.string.replace('Foodora',keyword))
       
    
 
    html = soup.prettify("utf-8")
    

    data.loc[i,'page']=filename
    data.loc[i,'url']=url
    data.loc[i,'ville']=villes.ix[i]['name']
    
    with open("/Users/makhtardiop/france/foodora/%s" % filename, "wb") as file:
        file.write(html)
    print ('Page   %s   Done' % filename)
    
        
    #print(result)
    # >>> <a href="index.html" id="websiteName">Foo</a>
    
    #result.string.replace_with('Bar')
    #print(result)
    # >>> <a href="index.html" id="websiteName">Bar</a>