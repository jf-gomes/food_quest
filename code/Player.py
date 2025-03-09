import pygame
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH

class Player:

    def __init__(self, name, startingPosition, entityList):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=startingPosition[0], top=startingPosition[1])
        self.entityList = entityList

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
    
    def checkFoodCollision(self):
        for food in self.entityList:
            if self.rect.colliderect(food):
                return food