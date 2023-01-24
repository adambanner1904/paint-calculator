import math


# Define a general space could be wall, window or door
class SquareSpace:

    # Initialise the space with a height and width
    def __init__(self, height, width):
        self.height = float(height)
        self.width = float(width)
        self.get_area()

    # Calculates the area of the space
    def get_area(self):
        self.area = self.height * self.width


class CircularSpace:

    # Initialise the space with a height and width
    def __init__(self, radius):
        self.radius = float(radius)

    # Calculates the area of the space
    def get_area(self):
        self.area = self.radius * math.pi


# A wall is a more specific definition of a space
# but inherits from a general space
class Wall(SquareSpace):

    # Initialise with the Space initialisation
    def __init__(self, height, width):
        SquareSpace.__init__(self, height, width)

    # Function to be used when adding a space to
    # recalculate the area
    def recalculate_area(self, space):
        self.area -= space.area

    # A function to add a space (window or door)
    # to the wall and will automatically subtract
    # the area
    def add_space(self, space):
        space.get_area()
        self.recalculate_area(space)

    # Works out the minimum and maximum amount of paint
    # required. The two values are the liters of paint
    # needed per meter squared
    def how_much_paint(self):
        self.min_liters_of_paint = 0.07143 * self.area
        self.max_liters_of_paint = 0.08333 * self.area

