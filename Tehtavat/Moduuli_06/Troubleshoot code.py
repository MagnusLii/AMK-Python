import math

def pizza_hinta_per_square_meter(diameter, price):
    return price / (math.pi * 2 * math.pow(diameter/2, 2))
pizza_hinta = []

for i in range(2):
    price = float(input(f"Anna {i + 1} pizzan hinnnan "))
    diameter = float(input(f"Anna {i + 1} pizzan halkaisijan "))
    pizza_hinta.append([pizza_hinta_per_square_meter(diameter, price), i+1])

print("Pizza 1 neliöhinta:", "{:.2f}".format(pizza_hinta[0][0]), "euroa")
print("Pizza 2 neliöhinta:", "{:.2f}".format(pizza_hinta[1][0]), "euroa")

pizza_hinta.sort(key=lambda x:x[0])
cheapest_pizza = pizza_hinta[0]

print("Halvin pizza on pizza numero", cheapest_pizza[1], "ja sen neliömetrin hinta on", "{:.2f}".format(cheapest_pizza[0]), "euroa per neliö")