import pygame

class SoundFactory:
    def __init__(self, name, type, extension, loop):
        self.name = name
        self.type = type
        self.extension = extension
        self.loop = loop

    def play(self):

        if self.type == 'songs':
            pygame.mixer.music.load(f'./assets/songs/{self.name}.{self.extension}')

        if self.loop and self.type == 'songs':
            pygame.mixer.music.play(-1)
        elif self.type == 'sounds':
            pygame.mixer.Sound(f'./assets/sounds/{self.name}.{self.extension}').play()

    def stop(self):
        pygame.mixer.music.stop()