import pygame
import math

from scripts.colors import *
from scripts.vector import Vector


class Line:
    def __init__(self, start_pos, end_pos, screen):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.screen = screen

    def draw(self):
        pygame.draw.line(self.screen, BLACK, self.start_pos, self.end_pos)

    def get_vector(self):
        return Vector(self.end_pos[0] - self.start_pos[0], self.end_pos[1] - self.start_pos[1])

    def get_points(self):
        for i in range(self.start_pos[0], self.end_pos[0]):
            for j in range(self.start_pos[1], self.end_pos[1]):
                if math.degrees(math.atan(j - self.start_pos[1] / i - self.start_pos[0])) == self.get_vector().get_angle():
                    print(True)
