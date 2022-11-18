from flask import Flask, Response
import json
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password="moodleroope",
         autocommit=True
         )
# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

app = Flask(__name__)
@app.route('/kenttä/<Koodi>')
def kenttä(Koodi):
    try:
        sql = "select name, municipality from airport where ident = '" + Koodi +"' "
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        Lentokenttä = (result[0][0])
        Kaupunki = (result[0][1])
        tilakoodi = 200
        vastaus = {
            "ICAO": Koodi,
            "Name": Lentokenttä,
            "Municipality": Kaupunki
        }



    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


