import nasdaqdatalink

import yfinance as yf

import pandas as pd

from pandas_datareader import data as pdr

def retrieveData(symbolsTotalInvestedDict):
    #mydata = nasdaqdatalink.get("WIKI/" + symbol, start_date="2018-01-30", end_date="2018-01-31")

    yf.pdr_override()

    print(symbolsTotalInvestedDict.keys())

    data = pdr.get_data_yahoo(list(symbolsTotalInvestedDict.keys()), period="1d")
    #data = pdr.get_data_yahoo('AAPL', start='2023-02-02', end='2024-02-02')

    print(data)

    adjCloseDF = data['Adj Close']

    

    masterLst = []
    
    print("*****************")
    for (retStockSymbol, retStockValue) in adjCloseDF.iteritems():
        masterDic = {}
        
        calculatedValues = []

        inputValues = symbolsTotalInvestedDict[retStockSymbol]

        masterDic['stockSymbol']   = retStockSymbol
        masterDic['numShares']     = inputValues[0]
        masterDic['totalInvested'] = inputValues[1]

        totalGain = round(float(float(inputValues[0]) * float(retStockValue))  - float(inputValues[1]), 2)
        masterDic['totalGain']       = "${:,.2f}".format(totalGain) #profit as of today 
        masterDic['percentGainLose'] = round((totalGain/float(inputValues[1])) * 100, 2)

        masterLst.append(masterDic)
        
        
    print("*****************")
    print(masterLst)
    print(adjCloseDF)
    print("*****************")

    return masterLst