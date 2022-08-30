while True:
    try:
        inch = float(input("Anna tuumien määrä: "))
    except ValueError:
        print("Syötä numero.")
        continue
    if inch < 0:
        print("Arvo on negatiivinen.\nExiting program.")
        exit()
    else:
        cm = inch * 2.54
        print(str(inch) +" tuuma on " +str(round(cm, 2)) +" cm.")