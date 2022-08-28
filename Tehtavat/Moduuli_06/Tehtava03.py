
userinput = 1

def conversion(gas):
    global liters
    liters = gas * 3.785411784
    print(round(liters,2))

while userinput >= 0:
    try:
        userinput = float(input("Anna gallonien määrä: "))
    except ValueError:
        print("Syötä numero.")
    else:
        if userinput < 0:
            exit()
        else:
            conversion(userinput)

