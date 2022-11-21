import mysql.connector
from flask import Flask, request, Response


app = Flask(__name__)

sqlconnect = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="flight_game",
    user="root",
    password="5579",
    autocommit=True
)


def cursor_fetchall(query):
    sqlcursor = sqlconnect.cursor()
    sqlcursor.execute(query)
    outcome = sqlcursor.fetchall()
    return outcome


@app.route('/kenttä/<ICAO>')
def geticao(ICAO):
    query = f'''SELECT name, municipality
            FROM airport
            WHERE ident = "{ICAO}"
            ;'''
    result = cursor_fetchall(query)
    for row in result:
        name = row[0]
        munici = row[1]
    json = {
        "ICAO": "EFHK",
        "name": name,
        "Municipality": munici
    }
    return json


if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)
