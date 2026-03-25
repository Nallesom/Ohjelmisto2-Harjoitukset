from flask import Flask, request, Response
import json
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='nalle',
    password='sup3rS!!st1',
    autocommit=True
)

cursor = connection.cursor()
app = Flask(__name__)
@app.route('/kenttä/<icao_code>')
def kenttä(icao_code):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao_code}';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:
        reponse = {
            "status": 400,
            "teksti": "Airport not found"
        }
        json_vastaus = json.dumps(reponse)
        return Response(response=json_vastaus, status=400, mimetype="application/json")

    return {"ICAO": icao_code, "Name": result[0][0], "Municipality": result[0][1]}

app.run(use_reloader=True, host='127.0.0.1', port=5555)