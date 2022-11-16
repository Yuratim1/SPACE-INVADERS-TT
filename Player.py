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
        self.ready_laser = True
        self.laser_timer = 0
        self.laser_cooldown = 600
        
    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < self.constraint:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            
        if keys[pygame.K_SPACE] and self.ready_laser:
            self.shoot_laser()
            self.ready_laser = False
            self.laser_timer = pygame.time.get_ticks()
            
    def recharge(self):
        if not self.ready_laser:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_timer >= self.laser_cooldown:
                self.ready_laser = True
    
    def shoot_laser(self):
        print('SHOOTING')
        
    def update(self):
        self.player_movement()
        self.recharge