import requests
import os

paikkakunta = input("Anna paikkakunta: ")

api_key = os.environ['WEATHER_API_KEY']

r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}").json()
print(r)
