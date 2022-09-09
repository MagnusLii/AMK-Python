# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
# senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
# pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä
# kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa
# paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

count = 0
i = 1


def pizzahinta(fdiameter, fprice):
    return fprice / (math.pi * 2 * math.pow(fdiameter/2, 2))


while count < 2:
    price = float(input(f"Anna {i} pizzan hinta: "))
    diameter = float(input(f"Anna {i} pizzan halkaisija: "))
    i += 1
    try:
        priceperarea = pizzahinta(diameter, price)
    except ValueError:
        print("Syötä numero!")
    else:
        print(f"Pizzan hinta per neliömetri on {round(pizzahinta(diameter, price), 2)}€.")
        if count == 0:
            price1 = round(priceperarea, 2)
        elif count == 1:
            price2 = round(priceperarea, 2)
        count += 1

if price1 == price2:
    print("Molemilla pizzoilla on sama hinta per bite.")
elif price1 < price2:
    print("Ekalla pizzalla on parempi hinta.")
else:
    print("Toisella pizzalla on parempi hinta.")
