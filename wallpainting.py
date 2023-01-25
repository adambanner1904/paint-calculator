from House import House
from Room import Room
from CircularSpace import CircularSpace
from RectangularSpace import RectangularSpace
from Wall import Wall


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
            height = float(input("What is the height of one of the walls?"))
            break
        except ValueError:
            print("Please enter a number as the height of your wall.")

    while True:
        try:
            width = float(input("What is the width of that wall"))
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
    prompt = " [Rectangle/Circle]"
    valid = {"rectangle": 0, "circle": 1}

    while True:
        choice = input(question + prompt).lower()
        if choice in valid:
            return valid[choice]
        else:
            print("Please choose one of the shapes.")


def query_obstruction_size(shape):

    if shape == 0:
        while True:
            try:
                height = float(input("What is the height of that obstruction"))
                break
            except ValueError:
                print("Please enter a number as the height of your obstruction.")
        while True:
            try:
                width = float(input("What is the width of that obstruction"))
                break
            except ValueError:
                print("Please enter a number as the width of your obstruction.")
        return height, width

    if shape == 1:
        while True:
            try:
                radius = float(input("What is the radius of that obstruction"))
                break
            except ValueError:
                print("Please enter a number as the radius of your obstruction.")
        return radius


def query_paint_price():
    if query_yes_no("Do you know how much your paint will cost? [Y/n]"
                    "(This program is more accurate if you can tell us the "
                    "exact amount your paint will cost.)"):
        while True:
            try:
                price = float(input("How much will it cost? (Please write it in the format '00.00'"))
                break
            except ValueError:
                print("Please enter a number as the amount")

        question = "What volume does the paint come in for that price?"
        prompt = " [1l, 2.5l, 5l, 10l] "
        valid = {"1": 1, "2.5": 2.5, '5': 5, '10': 10,
                 "1l": 1, "2.5l": 2.5, '5l': 5, '10l': 10,
                 "1 liter": 1, "2.5 liters": 2.5, '5 liters': 5, '10 liters': 10,
                 "1 litre": 1, "2.5 litres": 2.5, '5 litres': 5, '10 litres': 10}

        while True:
            choice = input(question + prompt).lower()
            if choice in valid:
                return valid[choice]
            else:
                print("Please choose one the volumes listed")
        return price, volume
    else:
        return 23, 2.5

def query_paint_brand():
    question = "What brand paint would you like to use? If your brand is none of these then enter " \
               "['n'/'none']"
    prompt = " [c = Crown/t = Tikkurila/d = Dulux/a = Armstead/m = Macpherson] "
    valid = {"c": 'Crown', "crown": "Crown", 't': 'Tikkurila', 'tikkurila': 'Tikkurila',
             'd': 'Dulux', 'dulux': 'Dulux', 'a': 'Armstead', 'armstead': 'Armstead',
             'm': 'Macpherson', 'macpherson': 'Macpherson', 'n': 'Average', 'none': 'Average'}

    while True:
        choice = input(question + prompt).lower()
        if choice in valid:
            return valid[choice]
        else:
            print("Please choose one of the brands listed or enter 'n' for none of those listed.")