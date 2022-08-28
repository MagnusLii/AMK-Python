import math

# Var
leiviskat = ""
naulat = ""
luodit = ""
rounded_gram = 0

# Functions used to weed out non numeric inputs from users.
def step1():                                            # Function 1
    for i in range(1):
        try:
            global leiviskat
            leiviskat = float(input("Anna leiviskät: "))# Asks for user input and coverts it into float.
        except ValueError:                              # If the conversion cannot be done the code gives further...
            print("syötä numero!")                      # instructions and returns to the start of the function.
            step1()
        else:
            step2()                                     # Else we move to the next function.

def step2():                                            # Function 2
    try:
        global naulat
        naulat = float(input("Anna naulat: "))
    except ValueError:
        print("syötä numero!")
        step2()
    else:
        step3()

def step3():                                            # Function 3
    try:
        global luodit
        luodit = float(input("Anna luodit: "))
    except ValueError:
        print("syötä numero!")
        step3()

def rounddown(num):
    return math.floor(num / 1000) * 1000


# Code Go
step1()

#test
#print(leiviskat)
#print(naulat)
#print(luodit)

# Conversion
grams = 13.3 * (luodit + (32 * (naulat + (leiviskat * 20))))  # Variable that stores total grams.

if grams >= 999:
    rounded_gram = rounddown(grams)         # Creates a new variable that has the value of 'grams' rounded down to...
                                            # nearest 1000. Used to store value of kilograms.
    grams = grams - (rounded_gram)          # Removes the grams moved into 'rounded_gram' from 'grams'
    rounded_gram = rounded_gram / 1000      # Converts grams into kilos within 'rounded grams' var



print("Massa nykymittojen mukaan: ", end="")
print(str(round(rounded_gram)) +" kilogramma ja " + str(round(grams, 3)) + " grammaa.")