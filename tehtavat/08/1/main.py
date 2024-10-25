import mysql.connector
import os

conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='python_tehtavat',
    user='mikko',
    password=os.environ['MARIA_DB_PASSWORD'],
    autocommit=True
)

icao = input("Anna ICAO koodi: ")

query = f"SELECT name, municipality FROM airport WHERE ident='{icao}';"
kursori = conn.cursor()
kursori.execute(query)
tulos = kursori.fetchone()

if tulos:
    print("Nimi:", tulos[0])
    print("Sijainti:", tulos[1])
else:
    print("Ei tuloksia")
