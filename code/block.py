from game_constants import *
import pygame

class Block:

    def __init__(self, block_type, init_cell):
        self.type = block_type
        self.filename = f"../media/images/blocks/{self.type}.png"
        self.img = None
        self.load_img()
        self.cell = init_cell
        self.row = self.cell[0]
        self.fraction = 0
        self.draw = True


    def raise_by_1(self, level = 1):
        if (self.fraction >= 1):
            self.row += 1
            _, col = self.cell
            self.cell = (self.row, col)
            self.fraction = 0
        else:
            #print(self.fraction)
            self.fraction += ((1/200)*0)

    def load_img(self):
        self.img = pygame.image.load(self.filename).convert_alpha()
        self.img = pygame.transform.scale(self.img, (BLOCK_WIDTH, BLOCK_HEIGHT))
