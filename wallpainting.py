import math


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


class CircularSpace:

    # Initialise the space with a height and width
    def __init__(self, radius):
        self.radius = float(radius)

    # Calculates the area of the space
    def get_area(self):
        self.area = self.radius * math.pi


# A wall is a more specific definition of a space
# but inherits from a general space
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
    def add_space(self, space):
        space.get_area()
        self.recalculate_area(space)

    # Works out the minimum and maximum amount of paint
    # required. The two values are the liters of paint
    # needed per meter squared
    def how_much_paint(self):
        self.min_liters_of_paint = 0.07143 * self.area
        self.max_liters_of_paint = 0.08333 * self.area


class Room:

    def __init__(self, name, num_of_walls):
        self.name = name
        self.num_of_walls = num_of_walls


class House:

    def __init__(self, num_of_rooms):
        self.num_of_rooms = num_of_rooms
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)


def query_num_rooms_in_house():
    while True:
        try:
            num_of_rooms = int(input("How many rooms do you want to paint? "))
            break
        except ValueError:
            print("Please enter a single number as the number of rooms that you want to paint")
    return House(num_of_rooms)


def query_and_add_room(house):

    name_of_room = input("What is the name of the room (Garage, living room, kitchen etc)?")

    while True:
        try:
            num_of_walls = int(input("How many walls need to be painted in this room?"))
            break
        except ValueError:
            print("Please enter a whole number of walls that need to be painted.")

    house.add_room(Room(name_of_room, num_of_walls))


def create_wall():
    print("What is the height and width of your wall")
    height = input("Height")
    width = input("Width")
    wall = Wall(height, width)
    return wall

def query_yes_no(question, default = "yes"):
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n":False}
    if default is None:
        prompt = " [y/n]"
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "

    while True:
        choice = input(question + prompt).lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no'")


def query_obstruction():
    while True:
        try:
            obstruction_yes_no = bool(input("Do you have a window or door (1 for yes, 0 for no)"))
            break
        except ValueError:
            print("Please enter a 1 for yes and a 0 for no.")
    return obstruction_yes_no

query_obstruction()
def query_shape_of_obstruction():
    shape_of_obstruction = input("Is your obstruction square or circular(1 for square, 0 for circular)")
    return shape_of_obstruction


def create_rectangular_obstruction(wall):
    obstruction_height = input("What is the height of your obstruction")
    obstruction_width = input("What is the width of your obstruction")
    wall.add_space(RectangularSpace(obstruction_height, obstruction_width))


def create_circle_obstruction(wall):
    radius = input("What is the radius of the obstruction")
    wall.add_space(CircularSpace(radius))




