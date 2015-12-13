# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:46:22 2015

@author: Harvey
"""

"""Did all 9 because, why not?"""
ssdDict = { \
    '0': [1,1,1,1,1,1,0,0], \
    '1': [0,1,1,0,0,0,0,0], \
    '2': [1,1,0,1,1,0,1,0], \
    '3': [1,1,1,1,0,0,1,0], \
    '4': [0,1,1,0,0,1,1,0], \
    '5': [1,0,1,1,0,1,1,0], \
    '6': [1,0,1,1,1,1,1,0], \
    '7': [1,1,1,0,0,0,0,0], \
    '8': [1,1,1,1,1,1,1,0], \
    '9': [1,1,1,1,0,1,1,0]}

def displayDigit(nDigit,pattern):
    print(pattern)

def displayStringOfNumbers(string,dictionary):
    for i in string:
        for j in dictionary:
            if i == j:
                displayDigit(i,dictionary[i])

def printHTTPheader():
    print('Content-type: text/html\r\n\r\n')

def latestReadings():
    import sqlite3 as lite

    con = lite.connect('weather.db')
    query = 'SELECT * FROM readings ORDER BY id DESC LIMIT 1'

    with con:
        con.row_factory = lite.Row

        cur = con.cursor()
        cur.execute(query)

        row = cur.fetchone()
        tpl = (row['id'], row['myDate'], row['mytime'], row['temperature'], row['humidity'])
        return tpl


def cleanString(string):
    return string[:-1]

displayStringOfNumbers('0123456789',ssdDict)
printHTTPheader()
print(latestReadings())
print(cleanString("Hi Jerome!"))