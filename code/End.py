from code.Background import Background
import pygame
from code.Const import WIN_HEIGHT, WIN_WIDTH, COLOR_PURPLE, MENU_OPTIONS
from code.Score import Score
from code.TxtFactory import TxtFactory

class End:

    def __init__(self, window, points):
        self.window = window
        self.points = points
        self.menuSelectedOptionId = 0

    def run(self, Level, Menu):
        
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.menuNavigation(event=event, Level=Level, Menu=Menu)

            self.window.blit(Background("menu_background_img").getBg(), (0, 0))

            txt = TxtFactory('boldonse', 24, (0, 0, 0), WIN_WIDTH // 2, WIN_HEIGHT // 2, 'Game Over!', self.window)
            txt.write()

            self.displayEndOptions()

            pygame.display.update()

    def displayEndOptions(self):

        for menuOption in MENU_OPTIONS:
            
            if menuOption["id"] == self.menuSelectedOptionId:
                textColor = COLOR_PURPLE
            else:
                textColor = (0, 0, 0)
            
            txt = TxtFactory('boldonse', 24, textColor, WIN_WIDTH // 2, menuOption['y_position'], menuOption['txt_end_screen'], self.window)
            txt.write()

    def menuNavigation(self, event, Level, Menu):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.menuSelectedOptionId > 0:
                self.menuSelectedOptionId -= 1
            if event.key == pygame.K_DOWN and self.menuSelectedOptionId < 2:
                self.menuSelectedOptionId += 1
            if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 2:
                pygame.quit()
                quit()
            if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 1:
                score = Score(window=self.window, points=self.points, origin="end", level=Level, menu=Menu, namesToRegister=1)
                score.show()
            if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 0:
                level = Level(self.window)
                level.run(Menu=Menu)