#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:32:56 2019

@author: makhtardiop
"""

from iexfinance.stocks import get_historical_data
import sys

stock =sys.argv[1]


print ("getting data of %s" % stock)
history=get_historical_data(stock, output_format='pandas')
history.to_csv('/Users/makhtardiop/spy/%s.csv' % stock)
    