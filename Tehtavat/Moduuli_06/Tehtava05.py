
full_list = []


def removenum(numlist):
    templist = []
    for j in numlist:
        if j % 2 == 0:
            templist.append(j)
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
            for k in data:
                print(k, end=" ")
            exit()
        else:
            nro = int(nro)
    except ValueError:
        print("KOKONAISNUMERO!")
    else:
        full_list.append(nro)
