import pygame
from code.Const import MENU_OPTIONS, WIN_WIDTH, WIN_HEIGHT, COLOR_PURPLE
from code.Level import Level

class Menu:

    def __init__(self, window, menuSelectedOptionId = 0):
        self.window = window
        self.background = pygame.image.load('./assets/menu_background_img.png').convert_alpha()
        self.menuSelectedOptionId = menuSelectedOptionId
        self.logo = pygame.image.load("./assets/logo.png")

    def run(self):

        pygame.display.set_caption("Food Quest")
        
        pygame.font.init()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.menuSelectedOptionId = 0
                    if event.key == pygame.K_DOWN:
                        self.menuSelectedOptionId = 1
                    if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 1:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_RETURN and self.menuSelectedOptionId == 0:
                        level = Level(self.window)
                        level.run()

            self.window.blit(self.background, (0, 0))

            self.window.blit(self.logo, self.logo.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2)))

            self.displayMenuOptions()

            pygame.display.update()

    def displayMenuOptions(self):

        for menuOption in MENU_OPTIONS:
            font = pygame.font.Font(None, 50)
            if menuOption["id"] == self.menuSelectedOptionId:
                textColor = COLOR_PURPLE
            else:
                textColor = (0, 0, 0)
            text = font.render(menuOption["txt"], True, textColor)
            text_rect = text.get_rect(center=(WIN_WIDTH // 2, menuOption["y_position"]))
            self.window.blit(text, text_rect)