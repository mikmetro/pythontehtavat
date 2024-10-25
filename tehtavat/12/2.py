import requests
import os

paikkakunta = input("Anna paikkakunta: ")

api_key = os.environ['WEATHER_API_KEY']

r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&units=metric&appid={api_key}").json()

print(f"Lämpötila paikkakunnassa {paikkakunta} on {r["main"]["temp"]} celcius astetta")
