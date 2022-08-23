numbers = []



def getnumber():
    while True:
        number = input("Input number: ")
        if number.isdigit():
            numbers.append(number)
            return


for i in range(3):
    getnumber()

num1 = numbers[0]
num2 = ""
num3 = ""

addition = int(num1)+int(num1)
multiplication = ""
average = ""

print(addition)
print(multiplication)
print(average)