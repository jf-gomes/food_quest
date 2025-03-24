from code.Background import Background
import pygame
from code.Const import WIN_HEIGHT, WIN_WIDTH, COLOR_PURPLE, MENU_OPTIONS
from code.Score import Score

class End:

    def __init__(self, window, points, menuSelectedOptionId = 0):
        self.window = window
        self.menuSelectedOptionId = menuSelectedOptionId
        self.points = points

    def run(self, Level, Menu):
        
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.menuSelectedOptionId > 0:
                        self.menuSelectedOptionId -= 1
                    if event.key == pygame.K_DOWN and self.menuSelectedOptionId < 2:
                        self.menuSelectedOptionId += 1
                    if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 2:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 1:
                        score = Score(window=self.window, points=self.points, origin="end")
                        score.show()
                    if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 0:
                        level = Level(self.window)
                        level.run(Menu=Menu)
            

            self.window.blit(Background("menu_background_img").getBg(), (0, 0))

            font = pygame.font.Font(None, 50)
            text = font.render("Game Over", True, COLOR_PURPLE)
            text_rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
            self.window.blit(text, text_rect)

            self.displayEndOptions()

            pygame.display.update()

    def displayEndOptions(self):

        for menuOption in MENU_OPTIONS:
            font = pygame.font.Font(None, 50)
            if menuOption["id"] == self.menuSelectedOptionId:
                textColor = COLOR_PURPLE
            else:
                textColor = (0, 0, 0)
            text = font.render(menuOption["txt"], True, textColor)
            text_rect = text.get_rect(center=(WIN_WIDTH // 2, menuOption["y_position"]))
            self.window.blit(text, text_rect)