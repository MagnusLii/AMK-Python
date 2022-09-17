
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


def getICAOinf(icao):
    sql = f'''SELECT name, municipality
      FROM airport
      WHERE ident = "{icao}"'''
    #print(sql)
    cursor = sqlconnect.cursor()
    cursor.execute(sql)
    outcome = cursor.fetchall()
    return outcome


print(getICAOinf(input("Anna ICAO: ".upper())))
