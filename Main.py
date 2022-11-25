import pygame
import sys
import os
from Player import Player
import obstacles
from aliens import Aliens, Bonusalien
from random import choice, randint
from laser import Laser


class Game:
    def __init__(self):
        player_sprite = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT), SCREEN_WIDTH, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        #Health and Score
        self.lives = 3
        self.lives_surf = pygame.image.load(os.path.join('graphics', 'player.png')).convert_alpha()
        self.lives_x_start_pos = SCREEN_WIDTH - (self.lives_surf.get_size()[0] * 2 + 20)
        self.score = 0
        self.font = pygame.font.Font('graphics/Pixeltype.ttf', 35)

        #block setup
        self.shape = obstacles.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [int(num * (SCREEN_WIDTH / self.obstacle_amount)) for num in range(self.obstacle_amount)]
        print(self.obstacle_x_positions)
        self.create_mult_obstacles(self.obstacle_x_positions , x_start = SCREEN_WIDTH / 14, y_start = 480)

        #Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.aliens_setup( rows = 6, cols = 8)
        self.alien_direction = 1
        
        #bonus alien
        self.bonus_alien = pygame.sprite.GroupSingle()
        self.bonus_alien_spawn_time = randint(400, 800)
        


    def create_obstacles(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacles.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)
    
    def create_mult_obstacles(self, args, x_start, y_start):
        for offset_x in args:
            self.create_obstacles(x_start, y_start, offset_x)

    def aliens_setup(self, rows, cols, x_distance = 60, y_distance = 48, x_offset = 70, y_offset = 70):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                
                if row_index == 0: alien_sprite = Aliens('yellow', x, y)
                elif 1 <= row_index <= 2: alien_sprite = Aliens('green', x, y)
                else: alien_sprite = Aliens('red', x, y)
                self.aliens.add(alien_sprite)

    def alien_pos_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= SCREEN_WIDTH:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)
    
    def alien_move_down(self, distance):
        if self.aliens:  
            for alien in self.aliens.sprites():
                alien.rect.y += distance
    
    def bonus_alien_time(self):
        self.bonus_alien_spawn_time -= 1
        if self.bonus_alien_spawn_time <= 0:
            self.bonus_alien.add(Bonusalien(choice(['right', 'left']), SCREEN_WIDTH))
            self.bonus_alien_spawn_time = randint(400,800)
    
    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, -6, SCREEN_HEIGHT)
            self.alien_lasers.add(laser_sprite)
            
    def collison_checks(self):
        
        #Player laser
        if self.player.sprite.bullet:
            for i in self.player.sprite.bullet:
                if pygame.sprite.spritecollide(i, self.blocks, True):
                    i.kill()
                
                alien_hit = pygame.sprite.spritecollide(i, self.aliens, True)
                if alien_hit:
                    for alien in alien_hit:
                        self.score += alien.value
                    i.kill()

                if pygame.sprite.spritecollide(i, self.bonus_alien, True):
                    i.kill()
                    self.score += 500
        #Alien Laser
        if self.alien_lasers:
            for i in self.alien_lasers:
                if pygame.sprite.spritecollide(i, self.player, False):           
                    i.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        pygame.quit()
                        sys.exit()

                elif pygame.sprite.spritecollide(i, self.blocks, True):
                    i.kill()
                
        if self.aliens:
            for i in self.aliens:
                pygame.sprite.spritecollide(i, self.blocks, True)

                if pygame.sprite.spritecollide(i, self.player, True):
                    pygame.quit()
                    sys.exit()

    def display_lives(self):
        for lives in range(self.lives - 1):
            x = self.lives_x_start_pos + (lives * (self.lives_surf.get_size()[0] + 10))
            screen.blit(self.lives_surf, (x, 8))
   
    def display_score(self):
        score_surf = self.font.render(f' Score: {self.score}', 1, 'white')
        score_rect = score_surf.get_rect(topleft = (10, 10))
        screen.blit(score_surf, score_rect)

    # update all sprite groups
    # draw all sprite groups
    def run(self):
        self.player.update()
        
        self.aliens.update(self.alien_direction)
        self.alien_pos_checker()
        self.alien_lasers.update()
        self.bonus_alien_time()
        self.bonus_alien.update()
        self.collison_checks()
        self.display_lives()
        self.display_score()

        self.player.sprite.bullet.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.bonus_alien.draw(screen)
        
        
        
if __name__ == '__main__':
    #Initial Setup
    pygame.init()

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    FPS = 60
    
    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")
    CLOCK = pygame.time.Clock()
    game = Game()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                game.alien_shoot()
    
        screen.fill((30, 30, 30))
        game.run()


        pygame.display.flip()
        CLOCK.tick(FPS)