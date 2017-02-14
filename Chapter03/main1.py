__author__ = 'Damien & Foreleser'

import pygame

# Screen Res
SCREEN_X = 640
SCREEN_Y = 480

# Start programmet
pygame.init()
pygame.display.set_mode((SCREEN_X, SCREEN_Y))


while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()
