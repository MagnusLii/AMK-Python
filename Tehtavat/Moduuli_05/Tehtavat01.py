import random

dice_amount = 0
rolls = []


# Loop to ask user for dice rolls and filter improper inputs.
while dice_amount == 0:
    try:
        dice_amount = int(input("Montakohan arpakuutiotta heitetään?: "))
    except ValueError:
        print("Syötä kokonaisluku.")


# Loop to generate dicerolls.
for x in range(dice_amount):
    rolls.append(random.randint(1,6))


sum_value = sum(rolls)
print(sum_value)




