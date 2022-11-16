import pygame
import os
import sys
from Player import Player
import obstaclesb


class Game:
    def __init__(self):
        player_sprite = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT), SCREEN_WIDTH, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        

    # update all sprite groups
    # draw all sprite groups
    def run(self):
        self.player.update()

        self.player.sprite.bullet.draw(screen)
        self.player.draw(screen)
        
        
        
if __name__ == '__main__':
    #Initial Setup
    pygame.init()

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    FPS = 60

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")
    CLOCK = pygame.time.Clock()
    game = Game()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        screen.fill((30, 30, 30))
        game.run()


        pygame.display.flip()
        CLOCK.tick(FPS)