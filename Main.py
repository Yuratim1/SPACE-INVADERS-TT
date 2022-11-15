# Main file to run the game

#IMPORTS
import pygame
import os
import sys

#Initial Setup
pygame.init()

screen_width = 400
screen_height = 400
fps = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((30, 30, 30))

    pygame.display.flip()
    clock.tick(60)