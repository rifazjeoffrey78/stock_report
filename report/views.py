from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "report/index.html")

def pullStockData(request, symbol):
    output = "APPLE data loading"
    return HttpResponse(output)

def pullStockData1(request):
    output = "NVDA data loading"
    return HttpResponse(output)