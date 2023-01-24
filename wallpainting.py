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
        self.walls = []

    def add_wall(self, wall):
        self.walls.append(wall)


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


def query_wall():

    while True:
        try:
            height = float(input("What is the height of your wall"))
            break
        except ValueError:
            print("Please enter a number as the height of your wall.")

    while True:
        try:
            width = float(input("What is the width of your wall"))
            break
        except ValueError:
            print("Please enter a number as the width of your wall.")

    return Wall(height, width)

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
    # Returns true if there is a obstruction on that wall and false if there isnt
    question = "Do you have a space in your wall like a window or door? " \
               "Press enter to answer yes by default"
    answer = query_yes_no(question)
    return answer


def query_shape_of_obstruction():
    # Returns 0 for rectangle and 1 for circle
    question = "What shape is your obstruction?"
    prompt = [" [Rectangle/Circle]"]
    valid = {"rectangle": 0, "circle": 1}

    while True:
        choice = input(question + prompt).lower()
        if choice in valid:
            return valid[choice]
        else:
            print("Please choose one of the shapes.")

def query_obstruction_size():
    pass

def create_rectangular_obstruction(wall):
    obstruction_height = input("What is the height of your obstruction")
    obstruction_width = input("What is the width of your obstruction")
    wall.add_space(RectangularSpace(obstruction_height, obstruction_width))


def create_circle_obstruction(wall):
    radius = input("What is the radius of the obstruction")
    wall.add_space(CircularSpace(radius))




