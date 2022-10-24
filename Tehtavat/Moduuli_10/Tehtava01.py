

class Elevator:
    def __init__(self, topfloor, bottomfloor = 0):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.currentfloor = bottomfloor

    def movetofloor(self, floortomoveto):
        #self.currentfloor = floortomoveto  # why do it the easy way...
        floorreached = False
        while not floorreached:
            if floortomoveto > self.currentfloor:
                print(f"Elevator moving up to floor {}")

    def floorup(self):
        self.currentfloor += 1

    def floordown(self):
        self.currentfloor -= 1
