
full_list = []

def removenum(list):
    templist = []
    for i in list:
        if i%2 == 0:
            templist.append(i)
    return templist

while True:
    try:
        nro = input("Syötä numero: ")
        nro = nro.lower()
        if nro == "exit":
            for i in full_list:
                print(i, end=" ")
            print()
            data = removenum(full_list)
            for i in data:
                print(i, end=" ")
            exit()
        else:
            nro = int(nro)
    except ValueError:
        print("KOKONAISNUMERO!")
    else:
        full_list.append(nro)