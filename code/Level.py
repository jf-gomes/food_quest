from code.Entity import Entity
import pygame
from code.EntityFactory import EntityFactory
from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH

class Level:

    def __init__(self, window):
        self.window = window

        self.entityList: list[Entity] = []
        self.entityList.append(EntityFactory.getEntity("player2"))

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
                if ent.name not in ["player_img_1", "player_img_2", "player_img_3"] and ent.rect.y >= 400 and ent.spawnArea == "top":
                    self.entityList.remove(ent)
                elif ent.name not in ["player_img_1", "player_img_2", "player_img_3"] and ent.rect.y >= 100 and ent.spawnArea == "bottom":
                    self.entityList.remove(ent)
                elif ent.name not in ["player_img_1", "player_img_2", "player_img_3"] and ent.rect.x >= 400 and ent.spawnArea == "left":
                    self.entityList.remove(ent)
                elif ent.name not in ["player_img_1", "player_img_2", "player_img_3"] and ent.rect.x >= 100 and ent.spawnArea == "right":
                    self.entityList.remove(ent)
                self.window.blit(source=ent.surf, dest=ent.rect)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == SPAWN_ITEM_EVENT:
                    self.entityList.append(EntityFactory.getEntity("food"))

            pygame.display.flip()

