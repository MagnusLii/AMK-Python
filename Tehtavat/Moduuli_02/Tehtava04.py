numbers = ["","",""]

def getnumber():
    for i in range(3):
        while True:
            number = input("Input number: ")
            if number.isdigit():
                numbers.append(number)

getnumber()

for x in numbers:
    print(x)

addition = ""
multiplication = ""
average = ""

print(addition)
print(multiplication)
print(average)