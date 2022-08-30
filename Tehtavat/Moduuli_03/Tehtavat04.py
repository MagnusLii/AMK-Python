
import math

while True:
    try:
        year = float(input("Anna vuosi: "))
        year = math.floor(year)
    except ValueError:
        print("Syötä numero.")
    else:
        break

if year % 400 == 0:
    print("The year " + str(year) + " is a leapyear")
elif year % 100 == 0:
    print("The year " + str(year) + " is not a leapyear")
elif year % 4 == 0:
    print("The year " + str(year) + " is a leapyear")
else:
    print("The year " + str(year) + " is not a leapyear")