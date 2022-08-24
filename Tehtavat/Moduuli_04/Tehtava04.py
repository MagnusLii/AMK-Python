
import random

# Var
value = random.randint(1,10)
guess = None

# Functions
def guess_func():
    global guess
    try:
        guess = float(input("Arvaa numero: "))
        return
    except ValueError:
        print("Syötä numero.")
        guess_func()

guess_func()
while True:
    if guess > value:
        print("Liian suuri arvaus.")
        #print(value)   # For troubleshooting.
        guess_func()
    elif guess < value:
        print("Liian pieni arvaus.")
        #print(value)   # For troubleshooting.
        guess_func()
    else:
        print("Oikein!")
        break