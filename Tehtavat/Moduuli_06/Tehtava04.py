
numbers = []

def summachine(list):
    return sum(list)

print("""Syötä "exit" kun olet syöttänyt kaikki numerot saadaksesi summa.""")

while True:
    try:
        nro = input("Syötä numero: ")
        nro = nro.lower()
        if nro == "exit":
            returnval = summachine(numbers)
            print(returnval)
            exit()
        else:
            nro = int(nro)
    except ValueError:
        print("KOKONAISNUMERO!")
    else:
        numbers.append(nro)