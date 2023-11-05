import pygame
from pygame import *
import random
from ship import Ship
from scenes import scene_handler
from scenes import Button
import time

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

crews = []
num_crews = 12

for i in range(1,num_crews+1):
    crews += [Ship(random.randrange(1, 31), random.randrange(1, 21), random.randrange(0, 1001))]

START = 0
SET = 1
MAIN = 2
BATTLE = 3
WIN = 4
LOSE = 5

state = 5


scene_handler = scene_handler(1,screen)

while running:
    scene_handler.present_scene()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()
pygame.quit()
