from abc import ABC

class Entity(ABC):

    def __init__(self, name: str, surf, rect, startingPosition):
        self.name = name
        self.surf = surf
        self.rect = rect
        self.startingPosition = startingPosition