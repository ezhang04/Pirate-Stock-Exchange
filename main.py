import pygame
from pygame import *
import random
from pygame_widgets.button import Button
from pirate import Pirate

pygame.init()
screen = pygame.display.set_mode((1250, 800))
clock = pygame.time.Clock()
running = True
button1 = Button(screen, 100, 100, 300, 150)
crew1 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))
crew2 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))
crew3 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))
crew4 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))
crew5 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))
crew6 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))
crew7 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))
crew8 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))
crew9 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))
crew10 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))
crew11 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))
crew12 = Pirate(random.randrange(1,31),random.randrange(1,21),random.randrange(0,1001))

start = 1
set = 2
main = 3
battle = 4
win = 5
lose = 6

state = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("red")
    if state == 1:
        screen.fill("blue")
    elif state == 2:
        screen.fill("blue")
    elif state == 3:
        screen.fill("blue")
    elif state == 4:
        screen.fill("blue")
    elif state == 5:
        screen.fill("blue")
    elif state == 6:
        screen.fill("blue")

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
