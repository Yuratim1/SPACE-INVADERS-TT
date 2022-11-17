import pygame
import sys
from Player import Player
import obstacles
import aliens


class Game:
    def __init__(self):
        player_sprite = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT), SCREEN_WIDTH, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.shape = obstacles.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [int(num * (SCREEN_WIDTH / self.obstacle_amount)) for num in range(self.obstacle_amount)]
        print(self.obstacle_x_positions)
        self.create_mult_obstacles(self.obstacle_x_positions , x_start = SCREEN_WIDTH / 14, y_start = 480)

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

    # update all sprite groups
    # draw all sprite groups
    def run(self):
        self.player.update()

        self.player.sprite.bullet.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        
        
        
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