import random
roll = None

def dicethrow():
    global roll
    roll = random.randint(1,6)

while roll != 6:
    dicethrow()
    print(roll)
    if roll == 6:
        exit()