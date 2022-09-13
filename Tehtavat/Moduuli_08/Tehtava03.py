
# Ohjelma hyödyntää komentoja/asetuksia Moduuli8/SQLfunctions.py tiedostostaan.
# Löytyy myös tästä AO linkistään.
# https://github.com/MagnusLii/ohjelmisto1/blob/master/Tehtavat/Moduuli_08/SQLfunctions.py

import geopy.distance
from SQLfunctions import cursor

coords = []


def getcoords(icao):
    query = f'''SELECT latitude_deg, longitude_deg 
        FROM airport WHERE ident = "{icao}"'''
    return cursor(query)


for i in range(2):
    userinp = (input(f"Give ICAO{i+1}: ").upper())
    coords.append(getcoords(userinp))

x = 0
for i in coords:
    item = coords[x]
    removelist = "[]()"
    for removelist in removelist:
        item = str(item)
        item = item.replace(removelist, "")
    coords[x] = item
    x += 1

print(f"The distance between the specified airports is {geopy.distance.geodesic(coords[0], coords[1])}")
