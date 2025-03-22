from code.Background import Background
import pygame
from DBProxy import DBProxy

class Score:

    def __init__(self, window):
        self.window = window

    def show(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.window.blit(Background("menu_background_img").getBg(), (0, 0))

            pygame.display.update()

    def save(self):
        db_proxy = DBProxy(db_name="game_data")
        