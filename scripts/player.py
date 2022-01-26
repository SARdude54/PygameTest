import pygame
import os


class Player:
    def __init__(self, x, y, screen: pygame.Surface):
        self.x = x
        self.y = y
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "player.png")), (50, 50))
        self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen = screen
        self.player = pygame.transform.scale(pygame.image.load(os.path.join("assets", "player.png")), (50, 50))

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def get_rect(self):
        return self.rect
