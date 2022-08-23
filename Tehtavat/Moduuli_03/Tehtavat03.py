gender = ""
hemo = ""

# Functions
def mies():
    global hemo
    if hemo <= 134:
        print("Hemoglobiinisi on matala.")
    elif hemo >= 195:
        print("Hemoglobiinisi on korkea.")
    else:
        print("Hemoglobiinisi on normaalia.")

def nainen():
    global hemo
    if hemo <= 117:
        print("Hemoglobiinisi on matala.")
    elif hemo >= 175:
        print("Hemoglobiinisi on korkea.")
    else:
        print("Hemoglobiinisi on normaalia.")

# Code start
# Sukupuoli kysely
while True:
    gender = input("Mikä on sukusi (mies/nainen)?: ")
    if gender.upper() in ["MIES","NAINEN"]:
        break
    else:
        print("Valitse yksi vaihtoehdoistaan.")
        exit()

# Hemoglobiiniarvo kysely
while True:
    try:
        hemo = float(input("Mikä on hemoglobiiniarvosi? (g/l): "))
    except ValueError:
        print("Syötä pelkkä numero, desimaalit ovat sallittua.")
        continue
    else:
        break

# Arvojen tarkistus
if gender.upper() in ["MIES"]:
    mies()
else:
    nainen()