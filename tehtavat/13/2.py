from flask import Flask, request
import mysql.connector
import os
import json

conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='python_tehtavat',
    user='mikko',
    password=os.environ['MARIA_DB_PASSWORD'],
    autocommit=True
)

app = Flask(__name__)
@app.route('/kentta/<icao>')
def lento_kentta(icao):
    query = f"SELECT name, municipality FROM airport WHERE ident='{icao}';"
    kursori = conn.cursor()
    kursori.execute(query)
    tulos = kursori.fetchone()
    if not tulos:
        return "Not found"
    return json.dumps({
        "ICAO": icao,
        "Name": tulos[0],
        "Municipality": tulos[1],
    })



if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=8532)
