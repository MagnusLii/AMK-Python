
import mysql.connector
import geopy.distance

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


coords = []

def getcoords(icao):
    query = f'''SELECT latitude_deg, longitude_deg 
        FROM airport WHERE ident = "{icao}"'''
    return cursor(query)


for i in range(2):
    userinp = (input(f"Give ICAO{i+1}: ").upper())
    coords.append(getcoords(userinp))

print(f"The distance between the specified airports is {geopy.distance.geodesic(coords[0], coords[1])}")
