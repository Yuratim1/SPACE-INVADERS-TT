import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, bullet_speed = 8, screen_height = 600):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('white') 
        self.rect = self.image.get_rect(center = pos)
        self.bullet_speed = bullet_speed
        self.y_constraint = screen_height

    def destroy(self):
        if self.rect.y <= 0 or self.rect.y >= self.y_constraint - 25:
            self.kill()
    
    def update(self):
        self.rect.y -= self.bullet_speed
        self.destroy()