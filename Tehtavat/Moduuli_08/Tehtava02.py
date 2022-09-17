
import mysql.connector

sqlconnect = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="flight_game1",
    user="pyth",
    password="1337",
    autocommit=True
)


def cursor(input):
    cursor = sqlconnect.cursor()
    cursor.execute(input)
    outcome = cursor.fetchall()
    return outcome


def getairporttype(country):
    query = f'''SELECT type, COUNT(type)
        FROM airport
        WHERE iso_country = "{country}"
        GROUP BY type
        HAVING COUNT(type) > 1
        ; '''
    cursor = sqlconnect.cursor()
    cursor.execute(query)
    outcome = cursor.fetchall()
    if cursor.rowcount > 0:
        return outcome
    else:
        print("Incorrect input.")
        exit()

print(getairporttype(input("Anna maan koodi: ".upper())))