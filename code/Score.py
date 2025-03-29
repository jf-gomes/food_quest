from code.Background import Background
import pygame
from code.DBProxy import DBProxy
from code.Const import WIN_HEIGHT, WIN_WIDTH, SCORE_TABLE_Y_POSITION, MENU_OPTIONS, COLOR_PURPLE
from datetime import datetime
from code.TxtFactory import TxtFactory

class Score:

    def __init__(self, window, points, origin, namesToRegister, level, menu):
        self.window = window
        self.points = points
        self.origin = origin
        self.namesToRegister = namesToRegister
        self.level = level
        self.menu = menu
        self.menuSelectedOptionId = 0

    def show(self):

        userName = ''

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.menuNavigation(event=event)
                if self.origin == "end":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            print(f"Nome inserido: {userName}")
                            self.save(userName=userName)
                            userName = ""
                            self.namesToRegister = 0
                        elif event.key == pygame.K_BACKSPACE:
                            userName = userName[:-1]
                        elif len(userName) < 4:
                            userName += event.unicode 

            self.window.blit(Background("level_background_img").getBg(), (0, 0))
            
            if self.origin == 'end' and self.namesToRegister == 1:

                txt1 = TxtFactory('openSans', 20, (0, 0, 0), WIN_WIDTH // 2, (WIN_HEIGHT // 2) + 100, 'DIGITE SEU NOME (ATÉ 4 CARACTERES)', self.window)
                txt1.write()

                txt2 = TxtFactory('openSans', 20, (0, 0, 0), WIN_HEIGHT // 2, (WIN_HEIGHT // 2) + 150, userName, self.window)
                txt2.write()

            dbProxy = DBProxy(db_name="game_data")
            playerList = dbProxy.retrieveTop10()

            if len(playerList) > 0:

                for n in range(len(playerList)):
                    txt = TxtFactory('openSans', 16, (0, 0, 0), WIN_WIDTH // 2, SCORE_TABLE_Y_POSITION[n]['y_position'], f'{n + 1} - Nome: {playerList[n][1]} | Pontos: {playerList[n][2]} | Data: {playerList[n][3]}', self.window)
                    txt.write()

            if self.namesToRegister == 0:
                self.displayMenuOptions()
                    
            pygame.display.update()

    def save(self, userName):
        db_proxy = DBProxy(db_name="game_data")
        db_proxy.save(name=userName, score=self.points, date=datetime.now().strftime("%d/%m/%Y") + " - " + datetime.now().strftime("%H:%M:%S"))

    def displayMenuOptions(self):

        for menuOption in MENU_OPTIONS:
            
            if menuOption["id"] == self.menuSelectedOptionId:
                textColor = COLOR_PURPLE
            else:
                textColor = (0, 0, 0)

            if menuOption['id'] != 1:
                txt = TxtFactory('boldonse', 24, textColor, WIN_WIDTH // 2, menuOption['y_position_score_screen'], menuOption['txt'], self.window)
                txt.write()

    def menuNavigation(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.menuSelectedOptionId = 0
            if event.key == pygame.K_DOWN:
                self.menuSelectedOptionId = 2
            if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 2 and self.namesToRegister == 0:
                pygame.quit()
                quit()
            if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 0 and self.namesToRegister == 0:
                level = self.level(self.window)
                level.run(Menu=self.menu)