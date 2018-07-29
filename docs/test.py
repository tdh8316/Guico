import pygame
from pygame.locals import *
import sys

# 1
display_width = 800
display_height = 600
pygame.init()
DISPLAY = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Guico Display (pygame)")
fps = pygame.time.Clock()

# define point

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    # 2
    DISPLAY.fill((255, 255, 255))

    # game

    pygame.display.update()
    fps.tick(60)