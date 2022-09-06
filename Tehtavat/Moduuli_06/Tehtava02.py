import random

roll = None

while True:
    try:
        dice = int(input("Nopan tahkojen määrä: "))
    except ValueError:
        print("KOKONAISLUKU!")
    else:
        break

while roll != dice:
    roll = random.randint(1, dice)
    print(roll)
    if roll == dice:
        exit()