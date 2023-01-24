from wallpainting import *

# Ask how many rooms are in the house
house = query_num_rooms_in_house()

# Loop through each room
for i in range(house.num_of_rooms):
    # Ask for the name of the house and the number of
    # walls that need to be painted in that room
    query_and_add_room(house)
    # Loop through each wall in the room
    for j in range(house.rooms[i].num_of_walls):
        # Add the wall to the room
        wall = query_wall()
        house.rooms[i].add_wall(wall)

        # If there is an obstruction then do this
        if query_obstruction():
            shape = query_shape_of_obstruction()
            if shape == 0:
                obstruction = query_obstruction_size()
                house.rooms[i].walls[j]
        # If no obstruction then carry on






# print("The area of your wall is " + str(round(wall1.area)) + " meters squared.")
#
# print("You will need between " + str(round(wall1.min_liters_of_paint, 2)) + " and " + str(
#     round(wall1.max_liters_of_paint, 2)) + " liters of paint to paint your wall once.")
