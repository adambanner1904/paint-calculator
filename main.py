from wallpainting import *
def query_obstruction():
    w_d = input("Do you have a window or door (1 for yes, 0 for no)")
    return w_d
def query_shape_of_obstruction():
    shape_of_obstruction = input("Is your obstruction square or circular(1 for square, 0 for circular)")
    return shape_of_obstruction

def create_square_obstruction():
    obs_h = input("What is the height of your obstruction")
    obs_w = input("What is the width of your obstruction")
    wall1.add_space(SquareSpace(obs_h, obs_w))

def create_circle_obstruction():
    radius = input("What is the radius of the obstruction")
    wall1.add_space(CircularSpace(radius))

def create_wall():
    print("What is the height and width of your wall")
    height = input("Height")
    width = input("Width")
    wall = Wall(height, width)






# print("The area of your wall is " + str(round(wall1.area)) + " meters squared.")
#
# print("You will need between " + str(round(wall1.min_liters_of_paint, 2)) + " and " + str(
#     round(wall1.max_liters_of_paint, 2)) + " liters of paint to paint your wall once.")
