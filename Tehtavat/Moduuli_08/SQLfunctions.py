
import mysql.connector

sqlconnect = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="flight_game1",
    user="root",
    password="5579",
    autocommit=True
)


def cursor(input):
    cursor = sqlconnect.cursor()
    cursor.execute(input)
    outcome = cursor.fetchall()
    return outcome
