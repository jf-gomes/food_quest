from code.Entity import Entity
import pygame
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH

class Player(Entity):

    def __init__(self, name, startingPosition):
        super().__init__(name, startingPosition)

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

        # Desenha elementos na tela
        # screen.blit(background, (0, 0))  # Fundo
        # screen.blit(character, character_rect)  # Personagem

        # Atualiza a tela
        # pygame.display.update()