from block import *
from game_constants import *
from random import randint

def euclid_x_to_column(x):
    for i in range(MAX_BLOCKS_X):
        minX, maxX = COLUMN_RANGES[i]
        if (x >= minX and x <= maxX):
            return i
    return -1

def euclid_y_to_row(y):
    for j in range(MAX_BLOCKS_Y):
        minY, maxY = ROW_RANGES[j]
        if (y >= minY and y <= maxY):
            return j
    return -1

class Grid:

    def __init__(self):
        self.rows = MAX_BLOCKS_Y
        self.cols = MAX_BLOCKS_X
        self.pool = ["goblin", "mander", "moon", "pig", "spiral", "star", "witch", "wizard"]
        self.block_list = None # 1D array of all blocks
        self.init_block_list()
        self.blocks_to_del = [] # 1D array of cells (row, col), used to take away matching blocks


    def del_blocks(self):
        return
        


    def init_block_list(self):
        self.block_list = []
        for j in range(self.rows):
            for i in range(self.cols):
                self.block_list.append(Block(self.pool[randint(0, 7)], (j, i)))
        

    def __getitem__(self, cell): # row first
        if (not self.block_list):
            raise ValueError("block grid is set to None")
        
        for b in self.block_list:
            if b.cell == cell:
                return b

        #print(f"no block at cell {cell}")

        raise IndexError(f"no block at cell {cell}")

    def __setitem__(self, key, value):
        if (self.block_list == None):
            raise ValueError("no block list")

        index=None
        for b in self.block_list:
            if (b.cell == key):
                index = self.block_list.index(b)
        if (not index):
            raise KeyError("improper key")
        self.block_list[index] = value

    def cell_to_euclid(self, cell):
        row = cell[0]
        col = cell[1]
        return (385 + (col * (50 + BLOCK_SPACING_X)), 805-PYGAME_TOP_BAR_HEIGHT-TEMPLATE_OFFSET_Y - row * (50 + BLOCK_SPACING_Y))

    def euclid_to_cell(self, euclid): # euclid is just point in xy-plane
        # used to convert mouse position on screen to cell in grid
        x = euclid[0]
        y = euclid[1]
        rowResult = euclid_y_to_row(y)
        columnResult = euclid_x_to_column(x)
        if (rowResult < 0):
            return (-1, -1)
        if (columnResult < 0):
            return (-1, -1)
        return (rowResult, columnResult)

    def swap_block_with_right_neighbor(self, cell_from_mouse):
        row, col = cell_from_mouse
        if (col + 1 >= MAX_BLOCKS_X):
            return
        
        indexA = -1
        indexB = -1
        try:
            for block in self.block_list:
                if (block.cell == cell_from_mouse):
                    indexA = self.block_list.index(block)

            for block in self.block_list:
                if (block.cell == (row, col + 1)):
                    indexB = self.block_list.index(block)

            self.block_list[indexA].cell = (row, col + 1)
            self.block_list[indexB].cell = cell_from_mouse

        except (IndexError) as e:
            raise ValueError(f"{cell_from_mouse} has no right neighbor!")

