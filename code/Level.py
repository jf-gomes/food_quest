import pygame
from code.FoodFactory import FoodFactory
from code.Background import Background
from code.End import End
from code.Player import Player
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Food import Food
from code.TxtFactory import TxtFactory

class Level:

    def __init__(self, window):
        self.window = window
        self.foodList: list[Food] = []
        self.player = Player(foodList=self.foodList, name="player_img_1", startingPosition=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.points = 0

    def run(self, Menu):
        
        SPAWN_ITEM_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(SPAWN_ITEM_EVENT, self.getSpawnTime())

        clock = pygame.time.Clock()

        pygame.font.init()
        
        while True:

            clock.tick(60)

            self.window.blit(Background("level_background_img").getBg(), (0, 0))

            self.window.blit(source=self.player.surf, dest=self.player.rect)

            self.player.move()

            playerFoodCollision = self.player.checkFoodCollision()

            for food in self.foodList:
                food.move()

                if food.checkCollision():
                    print(f'{food.name} leaving window area')
                    self.foodList.remove(food)

                if playerFoodCollision:
                    print(f'player catches {food.name}')
                    if playerFoodCollision.eatable:
                        self.foodList.remove(playerFoodCollision)
                        self.points += 1
                    else:
                        end = End(window=self.window, points=self.points)
                        end.run(Level=Level, Menu=Menu)
          
                self.window.blit(source=food.surf, dest=food.rect)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == SPAWN_ITEM_EVENT:
                    self.foodList.append(FoodFactory.getFood(speed=self.getSpeed()))

            txt = TxtFactory('boldonse', 16, (0, 0, 0), 100, 470, f'Pontuação: {str(self.points)}', self.window)
            txt.write()

            pygame.display.flip()

    def getSpeed(self):
        if self.points <= 10:
            return 7
        elif self.points <= 20:
            return 10
        elif self.points <= 30:
            return 12
        elif self.points <= 40:
            return 15
        elif self.points <= 40:
            return 20
        elif self.points <= 50:
            return 25
        
    def getSpawnTime(self):
        if self.points <= 10:
            return 3000
        elif self.points <= 20:
            return 2500
        elif self.points <= 30:
            return 2000
        elif self.points <= 40:
            return 1500
        elif self.points <= 40:
            return 1000
        elif self.points <= 50:
            return 500