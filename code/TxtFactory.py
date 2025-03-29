import pygame
from code.Const import MENU_OPTIONS, COLOR_PURPLE, WIN_WIDTH

class TxtFactory:
    
    def __init__(self, font, size, color, x_position, y_position, txt, window):
        self.font = font
        self.size = size
        self.color = color
        self.x_position = x_position
        self.y_position = y_position
        self.txt = txt
        self.window = window

    def write(self):
        font = pygame.font.Font(f'assets/fonts/{self.font}.ttf', self.size)
        text = font.render(self.txt, True, self.color)
        text_rect = text.get_rect(center=(self.x_position, self.y_position))
        self.window.blit(text, text_rect)