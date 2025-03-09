from code.Entity import Entity
import pygame
from code.EntityFactory import EntityFactory
from code.Background import Background

class Level:

    def __init__(self, window):
        self.window = window

        self.entityList: list[Entity] = []
        self.entityList.append(EntityFactory.getEntity("player1"))

    def run(self):

        spawnTime = 2000
        SPAWN_ITEM_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(SPAWN_ITEM_EVENT, spawnTime)

        clock = pygame.time.Clock()
        
        while True:

            clock.tick(60)

            self.window.blit(Background("level_background_img").getBg(), (0, 0))

            for ent in self.entityList:
                ent.move()
                if ent.checkCollision():
                    self.entityList.remove(ent)
                self.window.blit(source=ent.surf, dest=ent.rect)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == SPAWN_ITEM_EVENT:
                    self.entityList.append(EntityFactory.getEntity("food"))

            pygame.display.flip()

