import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, bullet_speed = 8):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('white') 
        self.rect = self.image.get_rect(center = pos)
        self.bullet_speed = bullet_speed
    
    def update(self):
        self.rect.y -= self.bullet_speed