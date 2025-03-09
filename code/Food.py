from code.Entity import Entity
import pygame
from code.Const import ENTITY_SPEED

class Food(Entity):

    def __init__(self, name, startingPosition, eatable: bool):
        super().__init__(name, startingPosition)

    def move(self):
        pass