# Main file to run the game

#IMPORTS
import pygame
import os
import sys

class Game:
    def __init__(self):
        pass

    # update all sprite groups
    # draw all sprite groups
    def run(self):
        pass

        
        
if __name__ == '__main__':
    #Initial Setup
    pygame.init()

    screen_width = 600
    screen_height = 600
    fps = 60

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    game = Game()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        screen.fill((30, 30, 30))
        game.run()


        pygame.display.flip()
        clock.tick(60)