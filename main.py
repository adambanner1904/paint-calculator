import math


# Define a general space could be wall, window or door
class SquareSpace:

    # Initialise the space with a height and width
    def __init__(self, height, width):
        self.height = float(height)
        self.width = float(width)

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


def query_obstruction():
    print("Do you have a window or door (1 for yes, 0 for no)")
    w_d = input()

    if int(w_d):
        print("Is your obstruction square or circular(1 for square, 0 for circular)")
        square_or_circular = input()
        if int(square_or_circular):
            print("What is the height of your obstruction")
            obs_h = input()
            print("What is the width of your obstruction")
            obs_w = input()
            wall1.add_space(SquareSpace(obs_h, obs_w))
        else:
            print("What is the radius of the obstruction")
            radius = input()
            wall1.add_space(CircularSpace(radius))


print("What is the height and width of your wall")
print("Height")
height = input()
print("Width")
width = input()

wall1 = Wall(height, width)
wall1.get_area()

query_obstruction()

wall1.how_much_paint()

print("The area of your wall is " + str(round(wall1.area)) + " meters squared.")

print("You will need between " + str(round(wall1.min_liters_of_paint, 2)) + " and " + str(
    round(wall1.max_liters_of_paint, 2)) + " liters of paint to paint your wall once.")

print("1")