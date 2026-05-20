from game_matrix import *
import pygame

class Renderer:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.template = pygame.image.load("../media/images/template.png")
        #self.background = pygame.image.load("../media/images/black_rect.png")
        self.grid = Grid() # initial grid of blocks

    def draw_blocks(self):
        rows = self.grid.rows
        cols = self.grid.cols

        for j in range(rows):
            for i in range(cols):
                cell = (j, i)
                pos = self.grid.cell_to_euclid(cell)
                x = pos[0]
                y = pos[1]
                self.screen.blit(self.grid[cell].img, (x, y))
    
    def redraw_screen(self):
        self.screen.fill((0, 0, 0))
        #self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.template, (0, 0))
        self.draw_blocks()
        pygame.display.flip()
