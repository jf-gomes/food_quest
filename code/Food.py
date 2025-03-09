from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT

class Food(Entity):

    def __init__(self, name, startingPosition, eatable: bool, spawnArea: str):
        super().__init__(name, startingPosition)
        self.spawnArea = spawnArea
        self.eatable = eatable

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

    def checkCollision(self):
        return self.rect.y >= WIN_HEIGHT and self.spawnArea == "top" or self.rect.y <= 0 and self.spawnArea == "bottom" or self.rect.x >= WIN_WIDTH and self.spawnArea == "left" or self.rect.x <= 0 and self.spawnArea == "right"