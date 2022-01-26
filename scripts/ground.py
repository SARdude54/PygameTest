import pygame
import os

from scripts.colors import *


class GroundBlock:
    def __init__(self, x, y, screen: pygame.Surface):
        self.x = x
        self.y = y
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "ground_block2.png")), (50, 50)).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y - 10
        self.screen = screen
        self.img.set_colorkey(WHITE)

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def get_rect(self):
        return self.rect
