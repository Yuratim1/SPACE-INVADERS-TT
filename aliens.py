import pygame
import os

class Aliens(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        file_name = color + 'png'
        self.image = pygame.image.load(os.path.join('graphics', file_name)).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x, y))
