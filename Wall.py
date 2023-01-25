from RectangularSpace import RectangularSpace
from CircularSpace import CircularSpace

class Wall(RectangularSpace):

    # Initialise with the Space initialisation
    def __init__(self, height, width):
        RectangularSpace.__init__(self, height, width)

    # Function to be used when adding a space to
    # recalculate the area
    def recalculate_area(self, space):
        self.area -= space.area

    # A function to add a space (window or door)
    # to the wall and will automatically subtract
    # the area
    def add_space(self, parameters):

        if isinstance(parameters, tuple):

            space = RectangularSpace(parameters[0], parameters[1])

        else:
            space = CircularSpace(parameters)
        space.get_area()
        self.recalculate_area(space)

    # Works out the minimum and maximum amount of paint
    # required. The two values are the liters of paint
    # needed per meter squared
    def how_much_paint(self):
        self.min_liters_of_paint = 0.07143 * self.area
        self.max_liters_of_paint = 0.08333 * self.area

