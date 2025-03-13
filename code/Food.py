from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
import pygame

class Food:

    def __init__(self, name, startingPosition: tuple, eatable: bool, spawnArea: str, speed):
        self.name = name
        self.startingPosition = startingPosition
        self.eatable = eatable
        self.spawnArea = spawnArea
        self.speed = speed
        
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=startingPosition[0], top=startingPosition[1])

    def move(self):
        match self.spawnArea:
            case "top":
                self.rect.centery += self.speed
            case "left":
                self.rect.centerx += self.speed
            case "right":
                self.rect.centerx -= self.speed
            case "bottom":
                self.rect.centery -= self.speed

    def checkCollision(self):
        return self.rect.y >= WIN_HEIGHT and self.spawnArea == "top" or self.rect.y <= 0 and self.spawnArea == "bottom" or self.rect.x >= WIN_WIDTH and self.spawnArea == "left" or self.rect.x <= 0 and self.spawnArea == "right"