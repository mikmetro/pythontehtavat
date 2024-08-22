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

icao = input("Anna maa koodi: ")

query = f"SELECT type, COUNT(type) FROM airport WHERE iso_country='{icao}' GROUP BY type;"
kursori = conn.cursor()
kursori.execute(query)
tulos = kursori.fetchall()

if tulos:
    for i in tulos:
        print(f"{i[0]}: {i[1]}")
else:
    print("Ei tuloksia")
