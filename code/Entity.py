from abc import ABC, abstractmethod
import pygame

class Entity(ABC):

    def __init__(self, name: str, startingPosition: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=startingPosition[0], top=startingPosition[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def checkCollision(self):
        pass