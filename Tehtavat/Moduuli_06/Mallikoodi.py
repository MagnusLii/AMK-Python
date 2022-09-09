# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
# senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
# pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä
# kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa
# paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

countlist = ["ekan", "toisen"]
count = 0


def pizza_hinta_per_square_meter(fdiameter, fprice):
    return fprice / (math.pi * 2 * math.pow(fdiameter/2, 2))


while count < 2:
    i = 0
    price = float(input(f"Anna {i + 1} pizzan hinta: "))
    diameter = float(input(f"Anna {i + 1} pizzan halkaisija: "))
    i += 1
    try:
        priceperarea = pizza_hinta_per_square_meter(diameter, price)
    except ValueError:
        print("Syötä numero!")
    else:
        print(f"Pizzan hinta per neliömetri on {round(pizza_hinta_per_square_meter(diameter, price), 2)}€.")
        if count == 0:
            price1 = round(priceperarea, 2)
        elif count == 1:
            price2 = round(priceperarea, 2)
        count = count + 1

if price1 == price2:
    print(f"Molemilla pizzoilla on sama hinta per bite.")
elif price1 < price2:
    print(f"Ekalla pizzalla on parempi hinta.")
else:
    print(f"Toisella pizzalla on parempi hinta.")
