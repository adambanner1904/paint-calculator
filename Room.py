class Room:

    def __init__(self, name, num_of_walls):
        self.name = name
        self.num_of_walls = num_of_walls
        self.walls = []

    def add_wall(self, wall):
        self.walls.append(wall)
