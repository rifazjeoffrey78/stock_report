from django.urls import path

from . import views

app_name = "report"

urlpatterns = [
    path("", views.index, name="index"),

    path("volume", views.volume, name="volume"),
    
    # ex: /polls/5/
    #path("<symbol>/retrieve", views.pullStockData, name="pullStockData"),

    #path("pullStockData/<symbol>", views.pullStockData, name="pullStockData"),

    #path("<symbol>", views.pullStockData, name="retrieve"),

    path("submit/<symbol>", views.pullStockData, name="submit1"),

    path("submit/", views.pullStockData1, name="submit2"),

    path("submitVolume/", views.pullStockDataVolume, name="submitVol"),
]