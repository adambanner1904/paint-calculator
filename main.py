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

            parameters = query_obstruction_size(shape)

            house.rooms[i].walls[j].add_space(parameters)
        # If no obstruction then carry on

house.get_total_area()
price, volume = query_paint_price()
paint = Paint(price, volume)

print(f'Total area is {House.total_area}')
