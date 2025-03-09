from code.Player import Player
from code.Food import Food
import random
from code.Const import WIN_HEIGHT, WIN_WIDTH, FOOD_LIST

class EntityFactory:

    @staticmethod
    def getEntity(entityType: str, entityList):
        match entityType:
            case "food":
                foodId = random.randint(0, 7)
                side = random.choice(["left", "right", "top", "bottom"])
                if side == "left":
                    x = -50
                    y = random.randint(0, WIN_HEIGHT - 50)
                elif side == "right":
                    x = WIN_WIDTH + 50
                    y = random.randint(0, WIN_HEIGHT - 50)
                elif side == "top":
                    x = random.randint(0, WIN_WIDTH - 50)
                    y = -50
                elif side == "bottom":
                    x = random.randint(0, WIN_WIDTH - 50)
                    y = WIN_HEIGHT + 50
                return Food(name=FOOD_LIST[foodId]["name"], eatable=FOOD_LIST[foodId]["eatable"], startingPosition=(x, y), spawnArea=side)