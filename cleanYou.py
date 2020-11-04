#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 07:07:48 2019

@author: makhtardiop
"""
i=1
f=1
text=' '
with open("test.txt") as f:
    for line in f:
        if i == 3 :
            text= text+" "+ str(line)
            print (line)
    
        else:
            if i % 2 != 0 :
                text= text+" "+ str(line)
                print (line)
        i=i+1
        print (line)
    text_file = open("Output.txt", "w")

    text_file.write(text)

    text_file.close()
    #print (text)
i=1
f=1
text=' '   
with open("Output.txt") as f:
    for line in f:
      
        if i % 2 == 0 :
            text= text+" "+ str(line)
            #text=text + ' %s'
            print (line)
        i=i+1
        print (line)
    text=text.replace('\n', '')
    text_file = open("Output2.txt", "w")

    text_file.write(text)

    text_file.close()
    
    print (text)
    #print (text)
                