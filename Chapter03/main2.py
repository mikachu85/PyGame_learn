__author__ = 'Damien & Foreleser'

import pygame

SCREEN_X = 640
SCREEN_Y = 480
Bakgrunn = "Data/sushiplate.jpg"

pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
background = pygame.image.load(Bakgrunn)

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()

    screen.blit(background, (0,0))
    pygame.display.update()