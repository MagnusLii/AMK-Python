numbers = []

def getnumber():
    #print("getnum start")
    try:
        number = float(input("Input number: "))
    except ValueError:
        print("Enter a number!")
        getnumber()
    else:
        #print("else")
        numbers.append(number)
        return


for i in range(3):
    #print("for loop")
    getnumber()

num1 = float(numbers[0])
num2 = float(numbers[1])
num3 = float(numbers[2])

addition = num1+num2+num3
multiplication = num1*num2*num3
average = multiplication/3

print(addition)
print(multiplication)
print(average)