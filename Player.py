import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(os.path.join('graphics', 'player.png')).convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        
    def player_movement(self):
        pass