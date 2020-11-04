#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:31:42 2020

@author: makhtardiop
"""

import urllib.request, json
import datetime
import pandas as pd
import sys
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

stock= sys.argv[1]
print (stock)
datatick=pd.DataFrame(index=range(86400), columns=["mytime","symbol","companyName","primaryExchange","calculationPrice",
                           "open","openTime","close","closeTime","high","low","latestPrice",
                           "latestSource","latestTime","latestUpdate","latestVolume","iexRealtimePrice",
                           "iexRealtimeSize","iexLastUpdated","delayedPrice","delayedPriceTime",
                           "extendedPrice","extendedChange","extendedChangePercent","extendedPriceTime",
                           "previousClose","previousVolume","change","changePercent","volume","iexMarketPercent",
                           "iexVolume","avgTotalVolume","iexBidPrice","iexBidSize","iexAskPrice","iexAskSize",
                           "marketCap","peRatio","week52High","week52Low","ytdChange","lastTradeTime","isUSMarketOpen"]
)

"""

["symbol","companyName","primaryExchange","calculationPrice","open","openTime","close","closeTime","high","low","latestPrice","latestSource","latestTime","latestUpdate","latestVolume","iexRealtimePrice","iexRealtimeSize","iexLastUpdated","delayedPrice","delayedPriceTime","extendedPrice","extendedChange","extendedChangePercent","extendedPriceTime","previousClose","previousVolume","change","changePercent","volume","iexMarketPercent","iexVolume","avgTotalVolume","iexBidPrice","iexBidSize","iexAskPrice","iexAskSize","marketCap","peRatio","week52High","week52Low","ytdChange","lastTradeTime","isUSMarketOpen"]

{"symbol":"AAPL","companyName":"Apple, Inc.","primaryExchange":"ASNDAQ","calculationPrice":"close","open":null,"openTime":null,"close":null,"closeTime":null,"high":null,"low":null,"latestPrice":296.62,"latestSource":"Close","latestTime":"December 31, 2019","latestUpdate":1601549836351,"latestVolume":null,"iexRealtimePrice":null,"iexRealtimeSize":null,"iexLastUpdated":null,"delayedPrice":null,"delayedPriceTime":null,"extendedPrice":null,"extendedChange":null,"extendedChangePercent":null,"extendedPriceTime":null,"previousClose":298.75,"previousVolume":36359501,"change":2.15,"changePercent":0.00757,"volume":null,"iexMarketPercent":null,"iexVolume":null,"avgTotalVolume":26390705,"iexBidPrice":null,"iexBidSize":null,"iexAskPrice":null,"iexAskSize":null,"marketCap":1336387375533,"peRatio":24.96,"week52High":305.71,"week52Low":145,"ytdChange":0.8676601861564718,"lastTradeTime":1622984648344,"isUSMarketOpen":false}
"""

time = datetime.now()
for i in range(86400):
    urlIex="https://sandbox.iexapis.com/stable/stock/%s/quote?token=Tpk_1fced2f35aca4c91831a1645a1860b3e" % stock
    print(urlIex)
    with urllib.request.urlopen(urlIex) as url:
        data = json.loads(url.read().decode())
        datatick.loc[i]['mytime']=time
        for col in datatick.columns:
            if col != 'mytime':
                datatick.loc[i][col]=data[col]
        datatick.to_csv('%s-%s.csv' %(stock, today))
        print("%s  price was %s" % (i,data['latestPrice']))