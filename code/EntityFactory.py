from code.Player import Player
from code.Food import Food
import random
from code.Const import WIN_HEIGHT, WIN_WIDTH

class EntityFactory:

    @staticmethod
    def getEntity(entityType: str):
        match entityType:
            case "player1":
                return Player("player_img_1", (400,400))
            case "player2":
                return Player("player_img_2", (0,0))
            case "player1":
                return Player("player_img_3", (0,0))
            case "banana":
                return Food(name="banana", eatable=True, startingPosition=(random.randint(50, WIN_WIDTH - 50), random.randint(50, WIN_HEIGHT - 50)))