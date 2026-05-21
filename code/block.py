from game_constants import *
import pygame

class Block:

    def __init__(self, block_type, init_cell):
        self.type = block_type
        self.filename = f"../media/images/blocks/{self.type}.png"
        self.img = None
        self.load_img()
        self.cell = init_cell
        self.draw = True

    def update_cell(self, new_cell):
        self.cell = new_cell

    def load_img(self):
        self.img = pygame.image.load(self.filename).convert_alpha()
        self.img = pygame.transform.scale(self.img, (BLOCK_WIDTH, BLOCK_HEIGHT))
