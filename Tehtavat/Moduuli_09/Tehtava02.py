
class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def kiihdyta(self, speedchange):
        self.current_speed += int(speedchange)
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.top_speed:
            self.current_speed = self.top_speed


car1 = Car("ABC-420", 69)

problems_between_chair_and_keyboard = 0

try:
    car1.kiihdyta(input("Nopeus muutos: "))
except ValueError:
    problems_between_chair_and_keyboard += 1

attributes = vars(car1)
print(", ".join("%s: %s" % item for item in attributes.items()))
