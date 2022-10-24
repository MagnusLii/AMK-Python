

class Elevator:
    def __init__(self, topfloor, bottomfloor = 1):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.currentfloor = bottomfloor


    def floorup(self):
        self.currentfloor += 1


    def floordown(self):
        self.currentfloor -= 1


    def movetofloor(self, floortomoveto):
        #self.currentfloor = floortomoveto  # why do it the easy way...
        floorreached = False
        while not floorreached:
            if floortomoveto == self.currentfloor:
                print("You've reached your desired floor.")
                floorreached = True
            elif floortomoveto > self.currentfloor:
                print(f"Elevator moving up to floor {self.currentfloor  + 1}")
                self.floorup()
            elif floortomoveto < self.currentfloor:
                print(f"Elevator moving down to floor {self.currentfloor - 1}")
                self.floordown()
            else:
                print("HELP! You've entered realms beyond imagining and now see colours no man has ever seen...\n"
                      "What might they be capable of?\n"
                      "\n"
                      "Oh, and there's also fish people...")


hissi = Elevator(10, 1)
hissi.movetofloor(10)
hissi.movetofloor(1)