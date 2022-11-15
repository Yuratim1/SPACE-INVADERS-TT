import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        self.image = pygame.image.load(os.path.join('graphics', 'player.png')).convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.constraint = constraint
        self.bullet_vel = 4
        
    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < self.constraint:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            
        if keys[pygame.K_SPACE]:
            self.shoot_laser()
        
    
    def shoot_laser(self):
        pass    
        
    def update(self):
        self.player_movement()
        self.shoot_laser()