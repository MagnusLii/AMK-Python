import mysql.connector

sqlconnect = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="flight_game1",
    user="root",
    password="5579",
    autocommit=True
)


def getICAOinf(icao):
    sql = f'''SELECT name, municipality
      FROM airport
      WHERE ident = "{icao}"'''
    #print(sql)
    cursor = sqlconnect.cursor()
    cursor.execute(sql)
    outcome = cursor.fetchall()
    print(outcome)

print(getICAOinf(input("Anna ICAO: ".upper())))
