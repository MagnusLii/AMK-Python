# Lists
numbers = []                                        # List, just to make things complicated.

# Functions
def getnumber():
    #print("getnum start")
    try:
        number = float(input("Input number: "))     # Ask for number and convert into float.
    except ValueError:                              # Gives error and returns to start if user inputs invalid syntax
        print("Enter a number!")
        getnumber()
    else:
        #print("else")
        numbers.append(number)                      # Appends the number into the list.
        return

# Code start
for i in range(3):
    #print("for loop")
    getnumber()

# Variables
num1 = float(numbers[0])
num2 = float(numbers[1])
num3 = float(numbers[2])
addition = num1+num2+num3
multiplication = num1*num2*num3
average = multiplication/3

print(addition)
print(multiplication)
print(average)