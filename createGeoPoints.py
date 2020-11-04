#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:42:02 2019

@author: makhtardiop
"""

from math import cos, sin, atan2, sqrt, radians, degrees, asin, modf
import pandas as pd
import requests


# script for returning elevation from lat, long, based on open elevation data
# which in turn is based on SRTM
def get_elevation(lat, long):
    query = ('https://api.open-elevation.com/api/v1/lookup'
             f'?locations={lat},{long}')
    r = requests.get(query).json()  # json object, various ways you can extract value
    # one approach is to use pandas json functionality:
    elevation = pd.io.json.json_normalize(r, 'results')['elevation'].values[0]
    return elevation


def getPathLength(lat1,lng1,lat2,lng2):
    '''calculates the distance between two lat, long coordinate pairs'''
    R = 6371000 # radius of earth in m
    lat1rads = radians(lat1)
    lat2rads = radians(lat2)
    deltaLat = radians((lat2-lat1))
    deltaLng = radians((lng2-lng1))
    a = sin(deltaLat/2) * sin(deltaLat/2) + cos(lat1rads) * cos(lat2rads) * sin(deltaLng/2) * sin(deltaLng/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = R * c

    return d

def getDestinationLatLong(lat,lng,azimuth,distance):
    '''returns the lat an long of destination point 
    given the start lat, long, aziuth, and distance'''
    R = 6378.1 #Radius of the Earth in km
    brng = radians(azimuth) #Bearing is degrees converted to radians.
    d = distance/1000 #Distance m converted to km

    lat1 = radians(lat) #Current dd lat point converted to radians
    lon1 = radians(lng) #Current dd long point converted to radians

    lat2 = asin( sin(lat1) * cos(d/R) + cos(lat1)* sin(d/R)* cos(brng))

    lon2 = lon1 + atan2(sin(brng) * sin(d/R)* cos(lat1), 
           cos(d/R)- sin(lat1)* sin(lat2))

    #convert back to degrees
    lat2 = degrees(lat2)
    lon2 = degrees(lon2)

    return[lat2, lon2]




    
import math




def calculateBearing(lat1,lng1,lat2,lng2):
    '''calculates the azimuth in degrees from start point to end point'''
    startLat = math.radians(lat1)
    startLong = math.radians(lng1)
    endLat = math.radians(lat2)
    endLong = math.radians(lng2)
    dLong = endLong - startLong
    dPhi = math.log(math.tan(endLat/2.0+math.pi/4.0)/math.tan(startLat/2.0+math.pi/4.0))
    if abs(dLong) > math.pi:
         if dLong > 0.0:
             dLong = -(2.0 * math.pi - dLong)
         else:
             dLong = (2.0 * math.pi + dLong)
    bearing = (math.degrees(math.atan2(dLong, dPhi)) + 360.0) % 360.0;
    return bearing

def main(interval,azimuth,lat1,lng1,lat2,lng2):
    '''returns every coordinate pair inbetween two coordinate 
    pairs given the desired interval'''

    d = getPathLength(lat1,lng1,lat2,lng2)
    remainder, dist = math.modf((d / interval))
    counter = float(interval)
    coords = []
    coords.append([lat1,lng1])
    data=pd.DataFrame(index=range(0,int(dist)), columns=['lat','lon'])
    i=0
    for distance in range(0,int(dist)):
        coord = getDestinationLatLong(lat1,lng1,azimuth,counter)
        counter = counter + float(interval)
        elevation=get_elevation(coord[0], coord[1])
        data.loc[i]['lat']=coord[0]
        data.loc[i]['lon']=coord[1]
        data.loc[i]['elevation']=elevation
        data.to_csv('routes2.csv')
        print(data.ix[i])
        coords.append(coord)
        i=i+1
    coords.append([lat2,lng2])
    return coords

if __name__ == "__main__":
    #point interval in meters
    interval = 100.0
    #direction of line in degrees
    #start point

    lat1 = 48.891961
    lng1 = 2.229150
    #end point
    

    # basildon Point
    lat2 = 51.575710
    lng2 = 0.490817
    azimuth = calculateBearing(lat1,lng1,lat2,lng2)
    print (azimuth)
    coords = main(interval,azimuth,lat1,lng1,lat2,lng2)
    print (coords)