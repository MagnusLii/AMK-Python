
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
    print("Year " + str(year) + " is a leapyear")
elif year % 100 == 0:
    print("Year " + str(year) + " is not a leapyear")
elif year % 4 == 0:
    print("Year " + str(year) + " is a leapyear")
else:
    print("Year " + str(year) + " is not a leapyear")