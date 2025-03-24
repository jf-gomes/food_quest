from code.Background import Background
import pygame
from code.DBProxy import DBProxy
from code.Const import WIN_HEIGHT
from datetime import datetime

class Score:

    def __init__(self, window, points, origin):
        self.window = window
        self.points = points
        self.origin = origin

    def show(self):

        font = pygame.font.Font(None, 30)

        userName = ''

        top10Position = [
            70,
            90,
            110
        ]

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if self.origin == "end":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            print(f"Nome inserido: {userName}")
                            self.save(userName=userName)
                            userName = ""
                        elif event.key == pygame.K_BACKSPACE:
                            userName = userName[:-1]
                        elif len(userName) < 4:
                            userName += event.unicode 

            self.window.blit(Background("menu_background_img").getBg(), (0, 0))
            
            if self.origin == "end":

                text_surface = font.render("DIGITE SEU NOME (ATÉ 4 CARACTERES):", True, (0, 0, 0))

                self.window.blit(text_surface, (50, WIN_HEIGHT // 2))

                text_surface = font.render(userName, True, (0, 0, 0))

                self.window.blit(text_surface, (50, (WIN_HEIGHT // 2) + 50))

            playerList = DBProxy(db_name="game_data").retrieveTop10()

            for playerScore in playerList:

                playerListFont = pygame.font.Font(None, 20)

                id_, name, score, date = playerScore

                text_surface = playerListFont.render(f'{id_} - Jogador: {name} | Pontuação: {score} | Data: {date}', True, (0, 0, 0))

                self.window.blit(text_surface, (50, top10Position[id_ - 1]))

            pygame.display.update()

    def save(self, userName):
        db_proxy = DBProxy(db_name="game_data")

        now = datetime.now()

        db_proxy.save(name=userName, score=self.points, date=now.strftime("%d/%m/%Y") + " - " + now.strftime("%H:%M:%S"))
        