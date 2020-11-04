# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import json
import pickle

data=pd.read_csv('train.csv')
print ("Building relevant variable needed")

channels= set (data['channelGrouping'])
engagement=set (data['socialEngagementType'])
withdict=['geoNetwork','totals','trafficSource','vsits','device']
features={'channelGrouping': set(), 
          'date': set(),
          'device':['browser','operatingSystem','isMobile','deviceCategory'], 
          'fullVisitorId': set(), 
          'geoNetwork': ['continent','subContinent','country'],
          'sessionId': set(), 'socialEngagementType': set(),
          'totals': ['visits','hits','pageviews','bounces','newVisits','transactionRevenue'], 
          'trafficSource': ['campaign','source','medium','keyword'],
          'visitId': set(), 'visitNumber': set(), 'visitStartTime': set()}


alls=['date','transactionRevenue','channelGrouping','browser','operatingSystem','isMobile','deviceCategory', 
      'fullVisitorId','continent','subContinent','country',
          'sessionId', 'socialEngagementType',
          'visits','hits','pageviews','bounces','newVisits',
          'campaign','source','medium','keyword',
          'visitId','visitNumber','visitStartTime']

visit_features=['visits','hits','pageviews','bounces','newVisits']
geo_features=['geoNetwork','subContinent','country']
device_features=['browser','operatingSystem','isMobile','deviceCategory']
trafic_features=['campaign','source','medium','keyword']
channel_features=['(Other)','Affiliates','Direct','Display','Organic Search','Paid Search','Referral','Social']

"""
ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")
{'muffin': 'lolz', 'foo': 'kitty'}

"""
print ("Building rich dataFrame")
end=14306
end2=24756
# end of trainset-2.csv 24748
print ("reading train dataFrame")
end3=25460
ENDRICH=pickle.load(open( "/Users/makhtardiop/Development/Google/LOGS/endRich.p","rb"))
richdata=pd.read_csv('/Users/makhtardiop/Development/Google/TRAIN/dataLAST.csv')
#richdata=pd.DataFrame(index=range(len(data)), columns=alls)
i=len(data)
While i >= 0 :
    print (i)

    x=data.iloc[i]
    for column in data.columns :
        
        if column in withdict :
   
            json_acceptable_string = x[column].replace("'", "\"")
            featdict= json.loads(json_acceptable_string)
            # d = {u'muffin': u'lolz', u'foo': u'kitty'}
        
            #featdict=ast.literal_eval(str(x[column]))
            
            for element in features[column]:
                
                if element != 'newVisits':
                    
                    
                    if element != 'transactionRevenue':
                        
                        try :
                            richdata.iloc[i][element]=featdict[element]
                        except :
                            richdata.iloc[i][element]='pas'
                    else:
                        
                        try :
                            
                            richdata.iloc[i]['transactionRevenue']=featdict[element]
                            print ("transaction revenue found")
                            
                        except:
                            richdata.iloc[i]['transactionRevenue']=0
                    
                    
                else:
                    try :
                        richdata.iloc[i]['newVisits']=featdict[element]
                    except :
                        richdata.iloc[i][element]=0
                    
                            
        
            
        else :
            richdata.iloc[i][column]=x[column]
        
    i=i - 1   

    richdata.to_csv('/Users/makhtardiop/Development/Google/TRAIN/dataLAST2.csv')
    pickle.dump( i, open( "/Users/makhtardiop/Development/Google/LOGS/endRich.p", "wb" ) )
    pickle.dump( end3, open( "/Users/makhtardiop/Development/Google/LOGS/startRich.p", "wb" ) )
