import random

namelist = []

print("""Syötä "exit" kun olet syöttänyt kaikki numerot saadaksesi summa.""")

while True:
    newname = input("give me 'da names ya stupid 'umie!: ")
    if newname in namelist:
        print("Aiemmin syötetty nimi.")
    elif newname.lower() == "exit":
        break
    else:
        print("Uusi nimi")
    namelist.append(newname)

print("---Nimet listassa---")
for j in namelist:
    print(j)