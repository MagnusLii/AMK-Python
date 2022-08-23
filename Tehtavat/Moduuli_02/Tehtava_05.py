import math

# Var
leiviskat = ""
naulat = ""
luodit = ""

# Functions
def step1():
    for i in range(1):
        try:
            global leiviskat
            leiviskat = float(input("Anna leiviskät. "))
        except ValueError:
            print("syötä numero!")
            step1()
        else:
            step2()
def step2():
    try:
        global naulat
        naulat = float(input("Anna naulat. "))
    except ValueError:
        print("syötä numero!")
        step2()
    else:
        step3()
def step3():
    try:
        global luodit
        luodit = float(input("Anna luodit. "))
    except ValueError:
        print("syötä numero!")
        step3()

# Code Go
step1()

#test
#print(leiviskat)
#print(naulat)
#print(luodit)

# Conversion
conversion_into_grams = 13.3*(luodit+(32*(naulat+(leiviskat*20))))

if conversion_into_grams >= 999:
    rounded_gram = round(conversion_into_grams, -3)
    conversion_into_grams = conversion_into_grams - (rounded_gram)
    rounded_gram = rounded_gram / 1000



print("Massa nykymittojen mukaan: ", end="")
print(str(round(rounded_gram)) +" kilogramma ja " +str(round(conversion_into_grams,3)) +" grammaa.")