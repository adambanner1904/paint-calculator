from wallpainting import *

house = query_num_rooms_in_house()

for i in range(house.num_of_rooms):

    query_and_add_room(house)
    for j in range(house.rooms[i].num_of_walls):
        pass






# print("The area of your wall is " + str(round(wall1.area)) + " meters squared.")
#
# print("You will need between " + str(round(wall1.min_liters_of_paint, 2)) + " and " + str(
#     round(wall1.max_liters_of_paint, 2)) + " liters of paint to paint your wall once.")
