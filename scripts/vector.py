import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = math.sqrt(self.x**2 + self.y**2)
        try:
            self.angle = math.degrees(math.atan(self.y / self.x))
        except ZeroDivisionError as e:
            pass

    def __repr__(self):
        return f"{self.x, self.y}"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_magnitude(self):
        return self.magnitude

    def get_angle(self):
        try:
            return self.angle
        except AttributeError as e:
            pass