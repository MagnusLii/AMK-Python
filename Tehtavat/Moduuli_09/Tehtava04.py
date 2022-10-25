import math
import random

# vars
hourofrace = 0

class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speedkmh = 0
        self.distance_traveled = 0

    def kiihdyta(self, speedchange):
        self.current_speedkmh += int(speedchange)
        if self.current_speedkmh < 0:
            self.current_speedkmh = 0
        elif self.current_speedkmh > self.top_speed:
            self.current_speedkmh = self.top_speed

    def travel(self, timehours):
        # math.sqrt and ** so negative speeds don't reduce distance traveled.
        self.distance_traveled += int(timehours * math.sqrt(self.current_speedkmh ** 2))

cars = []
for i in range(10):
    cars.append(Car(f"ABC-{i}", random.randint(100, 201)))

someonewon = False
while not someonewon:
    for car in cars:
        car.kiihdyta(random.randint(-10, +15))
        car.travel(1)
        if car.distance_traveled >= 10000:
            print(f"{car.registration_number} has won the race, the race lasted {hourofrace} hours.")
            someonewon = True
            break
    hourofrace += 1

for i in cars:
    attributes = vars(i)
    print(", ".join("%s: %s" % item for item in attributes.items()))