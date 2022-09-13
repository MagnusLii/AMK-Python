
# Ohjelma hyödyntää komentoja/asetuksia Moduuli8/SQLfunctions.py tiedostostaan.
# Löytyy myös tästä AO linkistään.
# https://github.com/MagnusLii/ohjelmisto1/blob/master/Tehtavat/Moduuli_08/SQLfunctions.py

from SQLfunctions import sqlconnect

def getcoords(ICAO):
    query = f'''SELECT latitude_deg, longitude_deg 
        FROM airport WHERE ident = "{ICAO}"'''

icao1 = input("Give ICAO1: ").upper()
icao2 = input("Give ICAO2: ").upper()

