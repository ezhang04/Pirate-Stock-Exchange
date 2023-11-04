import pygame
from pygame import *
import random
from pygame_widgets.button import Button
from ship import Ship

pygame.init()
screen = pygame.display.set_mode((1250, 800))
clock = pygame.time.Clock()
running = True
button1 = Button(screen, 100, 100, 300, 150)

crews = []
num_crews = 50

for i in range(num_crews):
    crews += Ship(random.randrange(1, 31) + i, random.randrange(1, 21) + (2 * i), random.randrange(0, 1001) + i)

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
