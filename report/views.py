from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

import report.stockpull as stockpull

import sys



def index(request):
    print(request.POST)
    return render(request, "report/index.html")

def volume(request):
    print(request.POST)
    return render(request, "report/volume.html")

def pullStockData(request, symbol):
    output = "APPLE data loading"
    return HttpResponse(output)

def pullStockDataVolume(request):

    print("---------------")
    print(request.POST.get('stocksVolume'))
    print("---------------")

    stocks = request.POST.get('stocksVolume')

    df = stockpull.retrieveVolumeData(stocks)
    
    context = {"masterDict" : df}

    return render(request,"report/resultsVolume.html", context)

def pullStockData1(request):
    output = "NVDA data loading"
    print(request.POST)

    name = request.POST.getlist('stock')
    print("------------->" + name[0])

    value = request.POST.getlist('totalInvested')
    print(value)
    print(" ------------->" + value[0])

    numShares = request.POST.getlist('numShares')

    metaDataLst = []
    for i in range(len(name)):
        temp = []
        temp.append(numShares[i])
        temp.append(value[i])
        metaDataLst.append(temp)

    print(metaDataLst)

    namevalue = dict(zip(name, metaDataLst))

    print(namevalue)
    
    df = stockpull.retrieveData(namevalue)

    context = {"masterDict" : df}

    return render(request, "report/results.html", context)