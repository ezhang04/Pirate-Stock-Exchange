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


START = 0
SET = 1
MAIN = 2
BATTLE = 3
WIN = 4
LOSE = 5

state = 0

scene_handler = scene_handler(state, screen)

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    scene_handler.present_scene()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


