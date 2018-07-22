import pygame
import sys
from pygame.locals import *

# 1
pygame.init()
DISPLAY = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Guico Display (pygame)")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

        # 2

        pygame.display.update()
