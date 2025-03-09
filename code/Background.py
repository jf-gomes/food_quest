import pygame

class Background:

    def __init__(self, name):
        self.name = name

    def getBg(self):
        return pygame.image.load('./assets/' + self.name +  '.png').convert_alpha()