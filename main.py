from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


#@app.get("/cotacao")
#def cotacao_mensal():
#    cotacao = requests.get('https://economia.awesomeapi.com.br/json/all')
#    cotacao_dic = cotacao.json()
#    return {'Dollar: {}'.format(cotacao_dic['USD']['bid'])}


@app.get("/weather-forecast/5-days")
def weather_forecast():
    weather = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat=-15.78&lon=-47.93&appid=033f8ae1b29668af840cc665b4c209d1")
    weather_dic = weather.json()
    return weather_dic