from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
import pygame

class Food:

    def __init__(self, name, startingPosition: tuple, eatable: bool, spawnArea: str):
        self.name = name
        self.startingPosition = startingPosition
        self.eatable = eatable
        self.spawnArea = spawnArea
        
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=startingPosition[0], top=startingPosition[1])

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