from game_matrix import *
import pygame

class Renderer:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.template = pygame.image.load("../media/images/template.png")
        #self.background = pygame.image.load("../media/images/black_rect.png")
        self.grid = Grid() # initial grid of blocks
                
        CURSOR_SWAPPER = pygame.cursors.Cursor((BLOCK_WIDTH//2 - 1, BLOCK_HEIGHT//2 - 1), # middle of left block to swap
                                                pygame.image.load("../media/images/cursor.png").convert_alpha())
        wand = pygame.image.load("../media/images/wand.png").convert_alpha()
        wand = pygame.transform.scale(wand, (50, 50))
        WAND_CURSOR = pygame.cursors.Cursor((0, 0), wand)
        LASER_POINTER = pygame.image.load("../media/images/pointer.png")

        self.images = {"cursor swapper":CURSOR_SWAPPER, "laser pointer":LASER_POINTER, "wand cursor":WAND_CURSOR}

        #pygame.mouse.set_cursor(self.images["cursor swapper"])

    def draw_blocks(self):
        rows = self.grid.rows
        cols = self.grid.cols

        for j in range(rows):
            for i in range(cols):
                cell = self.grid[(j, i)].cell
                pos = self.grid.cell_to_euclid(cell)
                x = pos[0]
                y = pos[1]
                self.screen.blit(self.grid[cell].img, (x, y))
    
    def redraw_screen(self):
        self.screen.fill(COLOR_WHITE)
        self.screen.blit(self.template, (0, 0))
        self.draw_blocks()
        mouseX, mouseY = pygame.mouse.get_pos()
        

        cell_found = self.grid.euclid_to_cell((mouseX, mouseY))
        if (cell_found[0] < 0):
            pygame.mouse.set_cursor(self.images["wand cursor"])
        else:
            pygame.mouse.set_cursor(self.images["cursor swapper"])
            self.screen.blit(self.images["laser pointer"], (mouseX, mouseY))
        #pygame.display.flip()

