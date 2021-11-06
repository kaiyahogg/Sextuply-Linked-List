class Coordinate(self):
    def pos_x(self):
        return self.x


    def pos_y(self):
        return self.y


    def pos_z(self):
        return self.z

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z