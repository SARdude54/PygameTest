import pygame
import os
from pygame.locals import *

from scripts.colors import *


class Chicken:
    def __init__(self, x, y, screen: pygame.Surface):
        self.x = x
        self.y = y
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "chicken.png")), (50, 50))
        self.img.set_colorkey(BACKGROUND_COLOR)
        self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen = screen

    def draw(self):
        self.screen.blit(self.img, self.rect)

