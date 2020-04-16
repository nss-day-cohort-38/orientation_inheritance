class Vehicle:
    def __init__(self, color):
        self.main_color = color
        self.maximum_occupancy = 0

    def drive(self):
        print("the vehicle is driven")