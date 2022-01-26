import pygame
import math
from pygame.locals import *

from scripts.colors import *


class Circle:
    def __init__(self, x, y, radius, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen

    def draw_circle(self):
        pygame.draw.circle(self.screen, RED, (self.x, self.y), self.radius)

    def collide(self, x, y):
        if self.x - self.radius < x < self.x + self.radius:
            return True
        if self.y - self.radius < y < self.y + self.radius:
            return True
        return False

    def delete(self):
        pass

        # surf = pygame.Surface((self.radius*2, self.radius*2))
        # surf.set_colorkey(BACKGROUND_COLOR)
        # surf_rect = surf.get_rect()
        # surf_rect.x = self.x - self.radius
        # surf_rect.y = self.y - self.radius
        # self.screen.blit(surf, surf.get_rect())

