# Define a general space could be wall, window or door
class RectangularSpace:

    # Initialise the space with a height and width
    def __init__(self, height, width):
        self.height = float(height)
        self.width = float(width)
        self.area = 0
        self.get_area()

    # Calculates the area of the space
    def get_area(self):
        self.area = self.height * self.width
