import pygame
from point import *
from renderer import *

class Background:
    def __init__(self):

        self.position = Point()
        self.renderer = SpriteRenderer(pygame.image.load("resources/background.png"))

        self.position.x += self.renderer.width / 2
        self.position.y += self.renderer.height / 2

        self.active = True

        # self.y = 0
        # self.y2 = -self.image.get_height()

    def run(self):
        pass