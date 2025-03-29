import pygame
from code.Const import MENU_OPTIONS, WIN_WIDTH, WIN_HEIGHT, COLOR_PURPLE
from code.Level import Level
from code.Background import Background
from code.Score import Score
from code.TxtFactory import TxtFactory
from code.SoundFactory import SoundFactory

class Menu:

    def __init__(self, window):
        self.window = window
        self.menuSelectedOptionId = 0
        self.logo = pygame.image.load("./assets/logo.png")
        self.menuMusic = SoundFactory('menu_song', 'songs', 'wav', True)

    def run(self):

        pygame.display.set_caption("Food Quest")

        self.menuMusic.play()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.menuNavigation(event=event)

            self.window.blit(Background("menu_background_img").getBg(), (0, 0))

            self.window.blit(self.logo, self.logo.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2)))

            self.displayMenuOptions()

            pygame.display.update()

    def displayMenuOptions(self):

        for menuOption in MENU_OPTIONS:
            if menuOption["id"] == self.menuSelectedOptionId:
                textColor = COLOR_PURPLE
            else:
                textColor = (0, 0, 0)
            
            txt = TxtFactory('boldonse', 24, textColor, WIN_WIDTH // 2, menuOption['y_position'], menuOption['txt'], self.window)
            txt.write()

    def menuNavigation(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.menuSelectedOptionId > 0:
                self.menuSelectedOptionId -= 1
            if event.key == pygame.K_DOWN and self.menuSelectedOptionId < 2:
                self.menuSelectedOptionId += 1
            if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 2:
                pygame.quit()
                quit()
            if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 1:
                score = Score(window=self.window, points=0, origin="menu", level=Level, menu=Menu, namesToRegister=0)
                score.show()
            if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 0:
                self.menuMusic.stop()
                level = Level(self.window)
                level.run(Menu=Menu)