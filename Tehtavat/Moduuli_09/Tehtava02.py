
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

problems_between_chair_and_keyboard = 0  # Keeps track of user errors.

car1.kiihdyta(30)
car1.kiihdyta(70)
car1.kiihdyta(50)
print(f"Current speed is {car1.current_speed}")
car1.kiihdyta(-250)
print("\n**tire screeches**\nOH NOE YOU CRASHED!!!!\nWEE-OOOO WEEEE--OOOOO **police sirens**\n")
print(f"Current speed is {car1.current_speed}")