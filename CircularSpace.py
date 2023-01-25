import math


class CircularSpace:

    # Initialise the space with a height and width
    def __init__(self, radius):
        self.radius = float(radius)
        self.area = 0

    # Calculates the area of the space
    def get_area(self):
        self.area = self.radius**2 * math.pi
