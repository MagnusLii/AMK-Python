# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
# senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
# pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä
# kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa
# paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math
meemit = ["ovat", "tärkeitä"]
count = 0
i = 0


def pizzahinta(fdiameter, fprice):
    return fprice / (math.pi * fdiameter)


while count < 2:
    try:
        price = float(input(f"Anna {i+1} pizzan hinta: "))
        diameter = float(input(f"Anna {i+1} pizzan halkaisija: "))
        priceperarea = pizzahinta(diameter, price)
    except ValueError:
        print("Syötä numero!")
    else:
        print(f"Pizzan hinta per neliömetri on {round(pizzahinta(diameter, price), 2)}€.")
        if i == 0:
            price1 = round(priceperarea, 2)
            i += 1
        elif i == 1:
            price2 = round(priceperarea, 2)
        count += 1

if price1 == price2:
    print("Molemilla pizzoilla on sama hinta per bite.")
elif price1 < price2:
    print("Ekalla pizzalla on parempi hinta.")
else:
    print("Toisella pizzalla on parempi hinta.")
