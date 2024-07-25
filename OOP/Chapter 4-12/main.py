class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        is_x_inside = self.pos_x >= x_1 and self.pos_x <= x_2
        is_y_inside = self.pos_y >= y_1 and self.pos_y <= y_2
        if is_x_inside and is_y_inside:
            return True
        return False

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        pass