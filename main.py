import pygame
from pygame import *
import random
from ship import Ship
from scenes import scene_handler
import time

pygame.init()
screen = pygame.display.set_mode((1250, 800))
clock = pygame.time.Clock()
running = True
button1 = Button(screen, 100, 100, 300, 150)

crews = []
num_crews = 50

for i in range(num_crews):
    crews += [Ship(random.randrange(1, 31) + i, random.randrange(1, 21) + (2 * i), random.randrange(0, 1001) + i)]

START = 0
SET = 1
MAIN = 2
BATTLE = 3
WIN = 4
LOSE = 5

state = 0

scene_handler = scene_handler(0,screen)

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    scene_handler.present_scene()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    pygame_widgets.update(events)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
