
# Var
numbers = []
input1 = ""

# Listing user inputted numbers.
print("Voit lopettaa pelin jättämällä vastauskentän tyhjäksi.")
while True:
    try:
        input1 = float(input("Syötä numero: "))
    except ValueError:
        if input1 == "":    # Exits when user leaves input empty.
            break
        else:               # Gives error message and resets if user enters non numeric value.
            print("Error! Syötä vain numeroita.")
        continue
    else:                   # Appends user input to list and resets the variable to empty.
        numbers.append(input1)
        input1 = ""

if len(numbers) == 0:       # Exits game without errors incase user enters no values into list.
    exit()

# Extra var
largest_num = numbers[0]
smallest_num = numbers[0]

# Finding largest value.
for num in numbers:
    if num > largest_num:
        largest_num = num
    else:
        continue
print("The biggest number is " +str(largest_num))

# Finding smallest value.
for num in numbers:
    if num < smallest_num:
        smallest_num = num
    else:
        continue
print("The smallest number is " +str(smallest_num))