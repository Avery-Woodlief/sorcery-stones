from game_constants import *
import pygame

class Block:

    def __init__(self, block_type):
        self.type = block_type
        self.filename = f"../media/images/blocks/{self.type}.png"
        self.img = None
        self.load_img()

    def load_img(self):
        self.img = pygame.image.load(self.filename).convert_alpha()
        self.img = pygame.transform.scale(self.img, (BLOCK_WIDTH, BLOCK_HEIGHT))
