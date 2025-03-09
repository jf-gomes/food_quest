from code.Entity import Entity
import pygame
from code.EntityFactory import EntityFactory
from code.Background import Background
from code.End import End
from code.Player import Player
from code.Const import WIN_HEIGHT, WIN_WIDTH

class Level:

    def __init__(self, window):
        self.window = window

        self.entityList: list[Entity] = []
        self.player = Player(entityList=self.entityList, name="player_img_1", startingPosition=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.points = 0

    def run(self):

        spawnTime = 2000
        SPAWN_ITEM_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(SPAWN_ITEM_EVENT, spawnTime)

        clock = pygame.time.Clock()

        pygame.font.init()
        
        while True:

            clock.tick(60)

            self.window.blit(Background("level_background_img").getBg(), (0, 0))

            self.window.blit(source=self.player.surf, dest=self.player.rect)

            self.player.move()

            playerFoodCollision = self.player.checkFoodCollision()

            for ent in self.entityList:
                ent.move()

                if ent.checkCollision():
                    print("food leaving window area")
                    self.entityList.remove(ent)
                if not playerFoodCollision:
                    pass
                else:
                    self.entityList.remove(playerFoodCollision)
                    self.points += 1
          
                self.window.blit(source=ent.surf, dest=ent.rect)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == SPAWN_ITEM_EVENT:
                    self.entityList.append(EntityFactory.getEntity("food", self.entityList))

            font = pygame.font.Font(None, 50)
            text = font.render(str(self.points), True, (0, 0, 0))
            text_rect = text.get_rect(center=(50, 470))
            self.window.blit(text, text_rect)

            pygame.display.flip()

