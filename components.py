import time
import requests

def values(c = input("Dgite o nome da cidade: ")):
    city = c
    units= "metric"
    key_api = "82ab1660203ce1f7515518c6f7f5689a"
    return f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key_api}&lang=pt_br&units={units}"

def requisition():
    url = values()
    response = requests.get(url)
    data = response.json()
    return data

def weather(data):
     return print(f"                     Tempo: {data['weather'][0]['description'].upper()}")

def temp(data):
     return print (f" Temperatura: {data['main']['temp']}°C | Sensação termica {data['main']['feels_like']}°C | Miníma {data['main']['temp_min']}°C | Máxima {data['main']['temp_max']}°C")

def wilds(data):
     return print (f"                    Ventos: {Converter(data['wind']['speed'])}")
     
def Converter(value):
    return (f"{round(value*3.6, 2)} KM/H") 

def loading():
        delay = 0.5
        for i in range(2):
            print("Carregando  ", end="\r")
            time.sleep(delay)
            print("Carregando > ", end="\r")
            time.sleep(delay)
            print("Carregando >> ", end="\r")
            time.sleep(delay)
            print("Carregando >>> ", end="\r")
            time.sleep(delay)
         
def run():
     data = requisition()
     weather(data)
     loading()
     temp(data)
     loading()
     wilds(data)

run()