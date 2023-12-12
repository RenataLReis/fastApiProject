from fastapi import FastAPI
import requests
import matplotlib.pyplot as plt

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/currency-quote/all")
def quote():
    quote_response = requests.get('https://economia.awesomeapi.com.br/json/all')
    quote_dic = quote_response.json()
    return quote_dic

@app.get("/currency-quote/{currency}")
def quote(currency: str):
    quote_response = requests.get('https://economia.awesomeapi.com.br/json/all')
    quote_dic = quote_response.json()
    return quote_dic[currency]['bid']


@app.get("/currency-quote/30days/{currency}")
def quote(currency: str):
    quote_30days_response = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
    quote_30days_dic = quote_30days_response.json()
    quote_30days_list = [float(item['bid']) for item in quote_30days_dic]
    return quote_30days_list


@app.get("/currency-quote/30days/plot/{currency}")
def quote(currency: str):
    quote_30days_response = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
    quote_30days_dic = quote_30days_response.json()
    quote_30days_list = [float(item['bid']) for item in quote_30days_dic]
    plt.figure(figsize=(15, 5))
    plt.plot(quote_30days_list)
    return plt.show()


@app.get("/weather-forecast")
def weather_forecast():
    weather = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat=-15.78&lon=-47.93&appid=033f8ae1b29668af840cc665b4c209d1')
    weather_dic = weather.json()
    return weather_dic