import random

roll = None

while roll != 6:
    roll = random.randint(1, 6)
    print(roll)
    if roll == 6:
        exit()
