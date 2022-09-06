import math
countlist = ["ekan", "toisen"]
count = 0


# biground = diameter, hunnie = price
def pizzaNamNamCalc(biground, hunnie):
    return hunnie/(math.pi*((biground/2)**2))


while count < 2:
    try:
        priceperarea = pizzaNamNamCalc(float(input("Anna " + countlist[count] + " pizzan halkaisija senttimetreinä: ")),
                                       float(input("Anna " + countlist[count] + " pizzan hinta: ")))
        # Jos haluat tietää pizzan hinnan per neliömetri.
        #print("Pizzan hinta per neliömetri on " + str(round(priceperarea,2)) + "€.")
    except ValueError:
        print("Syötä numero!")
    else:
        if count == 0:
            price1 = str(round(priceperarea, 2))
        elif count == 1:
            price2 = str(round(priceperarea, 2))
        count = count + 1

if price1 == price2:
    print("Molemilla pizzoilla on sama hinta per bite.")
elif price1 < price2:
    print("Ekalla pizzalla on parempi hinta.")
else:
    print("Toisella pizzalla on parempi hinta.")
