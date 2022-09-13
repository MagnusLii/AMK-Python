
# Ohjelma hyödyntää komentoja/asetuksia Moduuli8/SQLfunctions.py tiedostostaan.
# Löytyy myös tästä AO linkistään.
# https://github.com/MagnusLii/ohjelmisto1/blob/master/Tehtavat/Moduuli_08/SQLfunctions.py

import SQLfunctions


def getICAOinf(icao):
    sql = f'''SELECT name, municipality
      FROM airport
      WHERE ident = "{icao}"'''
    #print(sql)
    cursor = SQLfunctions.sqlconnect.cursor()
    cursor.execute(sql)
    outcome = cursor.fetchall()
    return outcome


print(getICAOinf(input("Anna ICAO: ".upper())))
