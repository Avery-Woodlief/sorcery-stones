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
        self.block_grid = None
        self.init_block_grid()
        

    def init_block_grid(self):
        #self.block_grid = [[Block(self.pool[randint(0, 7)], (j, i)) for i in range(num_cols)] for j in range(num_rows)] # i columns, j rows
        self.block_grid = [[Block(self.pool[randint(0, 7)]) for i in range(self.cols)] for j in range(self.rows)] # i columns, j rows

    def __getitem__(self, cell): # row first
        if (not self.block_grid):
            return ValueError("block grid is set to None")
        row = cell[0]
        col = cell[1]
        return self.block_grid[row][col] # returns block at that cell

    def cell_to_euclid(self, cell):
        row = cell[0]
        col = cell[1]
        return (385 + (col * (50 + BLOCK_SPACING_X)), 805-PYGAME_TOP_BAR_HEIGHT-TEMPLATE_OFFSET_Y - row * (50 + BLOCK_SPACING_Y))

    def euclid_to_cell(self, euclid): # euclid is just point in xy-plane
        x = euclid[0]
        y = euclid[1]
        rowResult = euclid_y_to_row(y)
        columnResult = euclid_x_to_column(x)
        if (rowResult < 0):
            return (-1, -1)
        if (columnResult < 0):
            return (-1, -1)
        return (rowResult, columnResult)

