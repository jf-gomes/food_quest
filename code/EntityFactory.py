from code.Player import Player

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