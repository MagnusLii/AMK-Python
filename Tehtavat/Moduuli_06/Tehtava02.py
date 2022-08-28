import random

roll = None

def dicethrow(maxroll):
    global roll
    roll = random.randint(1,maxroll)

while True:
    try:
        dice = int(input("Nopan tahkojen määrä: "))
    except ValueError:
        print("KOKONAISLUKU!")
    else:
        break

while roll != dice:
    dicethrow(dice)
    print(roll)
    if roll == dice:
        exit()