class House:

    def __init__(self, num_of_rooms):
        self.num_of_rooms = num_of_rooms
        self.rooms = []
        self.areas = []
        self.total_area = 0

        self.min_liters_of_paint = 0
        self.max_liters_of_paint = 0

        self.min_tubs_of_paint = 0
        self.max_tubs_of_paint = 0

        self.min_cost = 0
        self.max_cost = 0

    def add_room(self, room):
        self.rooms.append(room)

    def get_total_area(self):
        for room in self.rooms:
            for wall in self.rooms[room].walls:
                self.areas.append(self.rooms[room].walls[wall].area)

        self.total_area = sum(self.areas)

    def how_much_paint(self):
        self.min_liters_of_paint = 0.07143 * self.total_area
        self.max_liters_of_paint = 0.08333 * self.total_area

    def cost_to_paint_house(self, paint):

        self.min_tubs_of_paint = self.min_liters_of_paint//paint.volume + 1
        self.max_tubs_of_paint = self.max_liters_of_paint//paint.volume + 1

        self.min_cost = self.min_tubs_of_paint * paint.price
        self.max_cost = self.max_tubs_of_paint * paint.price


