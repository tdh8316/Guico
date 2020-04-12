import pygame
from pygame.locals import *


class Window:
    def __init__(self, size, title):
        self.display_width = size[0]
        self.display_height = size[1]
        self.title = title
        self.loop = True

        pygame.init()
        self.display = pygame.display.set_mode(
            (self.display_width, self.display_height)
        )
        pygame.display.set_caption(self.title)
        self.fps = pygame.time.Clock()
