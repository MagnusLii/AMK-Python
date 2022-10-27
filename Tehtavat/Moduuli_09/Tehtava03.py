
import math

class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speedkmh = 0
        self.distance_traveled = 0

    def speedup(self, speedchange):
        self.current_speedkmh += int(speedchange)
        if self.current_speedkmh < 0:
            self.current_speedkmh = 0
        elif self.current_speedkmh > self.top_speed:
            self.current_speedkmh = self.top_speed

    def travel(self, timehours):
        # math.sqrt and ** so negative speeds don't reduce distance traveled.
        self.distance_traveled += int(timehours * math.sqrt(self.current_speedkmh ** 2))


car1 = Car("ABC-420", 69)
car1.distance_traveled = 2000
car1.current_speedkmh = 60

problems_between_chair_and_keyboard = 0  # Keeps track of user errors.

try:
    car1.speedup(input("Nopeuden muutos: "))
except ValueError:
    problems_between_chair_and_keyboard += 1

car1.travel(5)

attributes = vars(car1)
print("\n".join("%s: %s" % item for item in attributes.items()))
