#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:48:55 2019

@author: makhtardiop
"""
from bs4 import BeautifulSoup as soup
import sys



file='/Users/makhtardiop/page1.html'
html = open(file).read()
soup = soup(html, 'lxml')
platform=sys.argv[1]
town=sys.argv[2]
toreplace=sys.argv[3]
keyword='%s %s' % (platform, sys.argv[2])
print (keyword)
filename='Livreur-%s-%s.html' % (platform, town.replace(' ','-'))
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
         elen.string.replace_with(elen.string.replace(toreplace,keyword))
    

for elen in soup.findAll('h2'):
    #print(elen.string)
    if elen.string!= None:
         elen.string.replace_with(elen.string.replace(toreplace,keyword))
    
            
            
for elen in soup.findAll('h3'):
    #print(elen.string)
    if elen.string!= None:
         elen.string.replace_with(elen.string.replace(toreplace,keyword))
    

for elen in soup.findAll('h4'):
    #print(elen.string)
    if elen.string!= None:
         elen.string.replace_with(elen.string.replace(toreplace,keyword))
    

for elen in soup.findAll('h5'):
    #print(elen.string)
    if elen.string!= None:
         elen.string.replace_with(elen.string.replace(toreplace,keyword))
    

for elen in soup.findAll('a'):
    #print(elen.string)
    if elen.string!= None:
         elen.string.replace_with(elen.string.replace(toreplace,keyword))
    

for elen in soup.findAll('figcaption'):
    print(elen.string)
    if elen.string!= None:
         elen.string.replace_with(elen.string.replace(toreplace,keyword))
    
            
for elen in soup.findAll('title'):
    print(elen.string)
    if elen.string!= None:
         elen.string.replace_with(elen.string.replace(toreplace,keyword))
    
            
for elen in soup.findAll('p'):
    print(elen.string)
    if elen.string!= None:
         elen.string.replace_with(elen.string.replace(toreplace,keyword))
   

 
html = soup.prettify("utf-8")



with open("/Users/makhtardiop/france/stuart/%s" % filename, "wb") as file:
    file.write(html)
print ('Page   %s   Done' % filename)
soup=0