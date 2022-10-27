
class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def speedup(self, speedchange):
        self.current_speed += int(speedchange)
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.top_speed:
            self.current_speed = self.top_speed


car1 = Car("ABC-420", 69)

problems_between_chair_and_keyboard = 0  # Keeps track of user errors.

car1.speedup(30)
car1.speedup(70)
car1.speedup(50)
print(f"Current speed is {car1.current_speed}")
car1.speedup(-250)
print("\n**tire screeches**\n"
      "OH NOE YOU CRASHED!!!!\n"
      "WEE-OOOO WEEEE--OOOOO **police sirens**\n\n"
      f"Current speed is {car1.current_speed}")