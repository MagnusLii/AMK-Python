
import math


# Function to check if user input is a prime number.
def primecheck(n):
    number = n
    if number == 1 or number == 4:
        print(str(number) +" ei ole alkuluku.")
        exitmethod()
    elif number == 2 or number == 3:
        print(str(number) +" on alkuluku.")
        exitmethod()
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if (n%i) == 0:
                print(str(n) +" ei ole alkuluku.")
                exitmethod()
            else:
                print(str(n) +" on alkuluku.")
                exitmethod()


# For easily changing if the code keeps running after returning an answer.
def exitmethod():
    exit()
    #numtocheck()


# Asks for number and weeds out non integers.
def numtocheck():
    while True:
        try:
            primecheck(int(input("Syötä kokonaisluku: ")))
        except ValueError:
            print("KOKONAISLUKU!")


# Code start
numtocheck()