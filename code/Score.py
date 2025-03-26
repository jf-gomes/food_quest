from code.Background import Background
import pygame
from code.DBProxy import DBProxy
from code.Const import WIN_HEIGHT, WIN_WIDTH
from datetime import datetime
from code.TxtFactory import TxtFactory

class Score:

    def __init__(self, window, points, origin):
        self.window = window
        self.points = points
        self.origin = origin

    def show(self):

        userName = ''

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

            pygame.display.update()
            
            if self.origin == 'end':

                txt1 = TxtFactory('openSans', 20, (0, 0, 0), WIN_WIDTH // 2, (WIN_HEIGHT // 2) + 100, 'DIGITE SEU NOME (ATÉ 4 CARACTERES)', self.window)
                txt1.write()

                txt2 = TxtFactory('openSans', 20, (0, 0, 0), WIN_HEIGHT // 2, (WIN_HEIGHT // 2) + 150, userName, self.window)
                txt2.write()

            dbProxy = DBProxy(db_name="game_data")
            playerList = dbProxy.retrieveTop10()

            if len(playerList) > 0:

                for n in range(10):
                    print(playerList[n][0], playerList[n][1], playerList[n][2])
                    pygame.quit()
                    quit()

    def save(self, userName):
        db_proxy = DBProxy(db_name="game_data")
        db_proxy.save(name=userName, score=self.points, date=datetime.now().strftime("%d/%m/%Y") + " - " + datetime.now().strftime("%H:%M:%S"))
        