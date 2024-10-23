import requests

r = requests.get("https://api.chucknorris.io/jokes/random").json()
print(r["value"])
