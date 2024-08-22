import ssl
import mysql.connector
import os
from geopy.distance import distance

conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='python_tehtavat',
    user='mikko',
    password=os.environ['MARIA_DB_PASSWORD'],
    autocommit=True
)

icao1 = input("Anna eka ICAO koodi: ")
icao2 = input("Anna toka ICAO koodi: ")

query = f"SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident='{icao1}' OR ident='{icao2}';"
kursori = conn.cursor()
kursori.execute(query)
tulos = kursori.fetchall()

if tulos and kursori.rowcount == 2:
    print(f"Etäisyys {tulos[0][0]} ja {tulos[1][0]} välillä")
    lentokentta1koordinaatit = (tulos[0][1], tulos[0][2])
    lentokentta2koordinaatit = (tulos[1][1], tulos[1][2])
    print(f"{distance(lentokentta1koordinaatit, lentokentta2koordinaatit)}")
else:
    print("Ei tuloksia")
