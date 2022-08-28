
# Lists
user_numbers = []


# Recording user input.
while True:
    try:
        user_input = ""
        user_input = input("Syötä numero: ")
        if user_input == "":
            break
        user_input = float(user_input)
    except ValueError:
            print("Käytä numeroita!")
    else:
        user_numbers.append(user_input)


# Organizing and printing biggest numbers.
user_numbers.sort(reverse=True)
for i in range(5):
    print(user_numbers[i])