import requests
import json
import time

from animation import animation_time



def Converter(value):
    return (f"{value*3.6} KM|H") 
#Sistema metrico:metros, celsius.
units= "metric" 

#Chave API
chave_api = "82ab1660203ce1f7515518c6f7f5689a"

#cidade = input("Digite o nome da cidade: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q=rio de janeiro&appid={chave_api}&lang=pt_br&units={units}"

# Fazer uma requisição GET para a API e armazenar informacoes
response = requests.get(url)

# Converter a resposta em formato JSON
data = response.json()

#Armazenar dados/criando informacao, convertendo medida.
tempo = (f"         Tempo: {data['weather'][0]['description'].upper()}")
print(" \n ")
temperatura = (f"   Temperatura: {data['main']['temp']}°C | Sensação termica {data['main']['feels_like']}°C | Miníma {data['main']['temp_min']}°C | Máxima {data['main']['temp_max']}°C")
print(" \n ")
ventos = (f"        Ventos: {Converter(data['wind']['speed'])}")

#Teste:
print(tempo)
animation_time.loading()
print(temperatura)
animation_time.loading()
print(ventos)

   