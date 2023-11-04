import pygame
from pygame import *
import random
from pygame_widgets.button import Button
from ship import Ship
import scenes

pygame.init()
screen = pygame.display.set_mode((1250, 800))
clock = pygame.time.Clock()
running = True
button1 = Button(screen, 100, 100, 300, 150)

crews = []
num_crews = 50

for i in range(num_crews):
    crews += [Ship(random.randrange(1, 31) + i, random.randrange(1, 21) + (2 * i), random.randrange(0, 1001) + i)]

START = 1
SET = 2
MAIN = 3
BATTLE = 4
WIN = 5
LOSE = 6

state = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if state == 1:
        scenes.scene_start(screen)
    elif state == 2:
        scenes.scene_setup(screen)
    elif state == 3:
        scenes.scene_main(screen)
    elif state == 4:
        scenes.scene_battle(screen)
    elif state == 5:
        scenes.scene_win(screen)
    elif state == 6:
        scenes.scene_lose(screen)

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
