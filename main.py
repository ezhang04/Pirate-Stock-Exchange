import pygame
from pygame import *
import random

pygame.init()
screen = pygame.display.set_mode((1250, 800))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

    screen.fill("blue")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
