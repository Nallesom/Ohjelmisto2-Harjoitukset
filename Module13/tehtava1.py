from flask import Flask, request, Response
import json

def isPrime(value):
    try:
        wholevalue = int(value)
    except:
        wholevalue = 0
    foundnums = 0
    if (wholevalue < 2):
        foundnums += 1

    for value in range(2, wholevalue):
        if (wholevalue % value == 0):
            foundnums += 1

    if (foundnums > 0):
        return False
    else:
        return True

app = Flask(__name__)
@app.route('/alkuluku/<input>')
def alkuluku(input):
    try:
        luku = int(input)
        return {"Number": luku, "isPrime": isPrime(luku)}
    except ValueError:
        reponse = {
            "status": 400,
            "teksti": "Bad number"
        }
        json_vastaus = json.dumps(reponse)
        return Response(response=json_vastaus, status=400, mimetype="application/json")

app.run(use_reloader=True, host='127.0.0.1', port=5555)