
namelist = set()

while True:
    newname = input("give me 'da names ya stupid 'umie!: ")
    if newname in namelist:
        print("Aiemmin syötetty nimi.")
    elif newname.lower() == "":
        break
    else:
        print("Uusi nimi")
    namelist.add(newname)

print("---Nimet listassa---")
for j in namelist:
    print(j)
