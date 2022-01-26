import pygame
import sys
import time
import math
import os
from pygame.locals import *

from scripts.colors import *
from scripts.circle import Circle
from scripts.line import Line
from scripts.player import Player
from scripts.ground import GroundBlock
from scripts.chicken import Chicken

WIDTH, HEIGHT = (500, 500)

clock = pygame.time.Clock()
framerate = 60

pygame.display.set_caption("Square")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

last_time = time.time()

player = Player(WIDTH // 2, 400, screen)
player_rect = player.get_rect()

chicken = Chicken(50, 50, screen)

blocks = []

for i in range(0, WIDTH, 50):
    blocks.append(GroundBlock(i, 460, screen))

left = False
right = False
jumping = False
speed = 5
gravity = 5
jump_count = 1
jump = 20
is_air = False
throw = False
speed = 5
set_vector = None

running = True