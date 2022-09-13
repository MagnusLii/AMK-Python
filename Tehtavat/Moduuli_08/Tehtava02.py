
# Ohjelma hyödyntää komentoja/asetuksia Moduuli8/SQLfunctions.py tiedostostaan.
# Löytyy myös tästä AO linkistään.
# https://github.com/MagnusLii/ohjelmisto1/blob/master/Tehtavat/Moduuli_08/SQLfunctions.py

from SQLfunctions import sqlconnect

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