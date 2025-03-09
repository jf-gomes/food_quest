from code.Entity import Entity
from code.Const import ENTITY_SPEED

class Food(Entity):

    def __init__(self, name, startingPosition, eatable: bool, spawnArea: str):
        super().__init__(name, startingPosition)
        self.spawnArea = spawnArea

    def move(self):
        match self.spawnArea:
            case "top":
                self.rect.centery += ENTITY_SPEED[self.name]
            case "left":
                self.rect.centerx += ENTITY_SPEED[self.name]
            case "right":
                self.rect.centerx -= ENTITY_SPEED[self.name]
            case "bottom":
                self.rect.centery -= ENTITY_SPEED[self.name]

    def removeFood(self):
        pass