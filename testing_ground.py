from House import House
from Room import Room
from CircularSpace import CircularSpace
from RectangularSpace import RectangularSpace
from Wall import Wall
from Paint import Paint


house = House(4)
house.total_area = 120

house.how_much_paint()
paint = Paint(20, 2.5)
house.cost_to_paint_house(paint)
print(house.min_cost, house.max_cost)