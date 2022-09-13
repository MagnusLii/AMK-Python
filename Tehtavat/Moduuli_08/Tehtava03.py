
# Ohjelma hyödyntää komentoja/asetuksia Moduuli8/SQLfunctions.py tiedostostaan.
# Löytyy myös tästä AO linkistään.
# https://github.com/MagnusLii/ohjelmisto1/blob/master/Tehtavat/Moduuli_08/SQLfunctions.py

# TODO: update import model.
from geopy.distance import geodesic as GD
import geopy.distance

coords = []

from SQLfunctions import cursor


def getcoords(ICAO):
    query = f'''SELECT latitude_deg, longitude_deg 
        FROM airport WHERE ident = "{ICAO}"'''
    return cursor(query)

for i in range(2):
    userinp = (input(f"Give ICAO{i}: ").upper())
    coords.append(getcoords(userinp))


#icao1 = (input("Give ICAO1: ").upper())
#icao2 = (input("Give ICAO2: ").upper())
#icao1 = "AYMN" # (-6.14774, 143.656998)
#icao2 = "EFHK" # (60.3172, 24.963301)

#coords.append(getcoords(icao1))
#coords.append(getcoords(icao2))

x = 0
for i in coords:
    item = coords[x]
    removelist = "[]()"
    for removelist in removelist:
        item = str(item)
        item = item.replace(removelist, "")
    coords[x] = item
    x += 1

#print(coords[0])
#print(coords[1])
#print(coords)
#print(GD((-6.14774, 143.656998), (60.3172, 24.963301)))
print(f"The distance between the specified airports is {GD(coords[0], coords[1])}")