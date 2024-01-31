from django.urls import path

from . import views

app_name = "report"

urlpatterns = [
    path("", views.index, name="index"),
    
    # ex: /polls/5/
    #path("<symbol>/retrieve", views.pullStockData, name="pullStockData"),

    #path("pullStockData/<symbol>", views.pullStockData, name="pullStockData"),

    #path("<symbol>", views.pullStockData, name="retrieve"),

    path("submit/<symbol>", views.pullStockData, name="submit"),

    path("submit/", views.pullStockData1, name="submit"),
]