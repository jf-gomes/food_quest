from code.Entity import Entity
import pygame
from code.EntityFactory import EntityFactory
import random
from code.Const import WIN_HEIGHT, WIN_WIDTH, FOOD_NAMES

class Level:

    def __init__(self, window):
        self.window = window
        self.background = pygame.image.load('./assets/level_background_img.png').convert_alpha()

        self.entityList: list[Entity] = []
        self.entityList.append(EntityFactory.getEntity("player1"))

    def run(self):

        SPAWN_ITEM_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(SPAWN_ITEM_EVENT, 2000)

        clock = pygame.time.Clock()
        
        while True:

            clock.tick(60)

            self.window.blit(self.background, (0, 0))

            for ent in self.entityList:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == SPAWN_ITEM_EVENT:
                    self.entityList.append(EntityFactory.getEntity("banana"))
                    print("banana adicionada")

            pygame.display.flip()

