# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
# senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
# pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä
# kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa
# paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

countlist = ["ekan", "toisen"]
count = 0


def pizza_hinta_per_square_meter(diameter, price):
    return price / (math.pi * 2 * math.pow(diameter/2, 2))


while count < 2:
    for i in range(1):
        price = float(input(f"Anna {i + 1} pizzan hinta: "))
        diameter = float(input(f"Anna {i + 1} pizzan halkaisija: "))
        try:
            priceperarea = pizza_hinta_per_square_meter(diameter, price)
        except ValueError:
            print("Syötä numero!")
        else:
            if count == 0:
                price1 = str(round(priceperarea, 2))
            elif count == 1:
                price2 = str(round(priceperarea, 2))
            count = count + 1

if price1 == price2:
    print(f"Molemilla pizzoilla on sama hinta per bite. Hinta on {price1}€.")
elif price1 < price2:
    print(f"Ekalla pizzalla on parempi hinta. Pizzan hinta per neliömetri on {price1}€.")
else:
    print(f"Toisella pizzalla on parempi hinta. Pizzan hinta per neliömetri on {price2}€.")