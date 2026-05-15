from block import *
from random import randint

def init_game_matrix(num_rows, num_cols):
    pool = ["goblin", "mander", "moon", "pig", "spiral", "star", "witch", "wizard"]
    #pool = ["goblin", "goblin", "goblin", "goblin", "wizard", "wizard", "wizard", "wizard"]

    gameMatrix = [[Block(pool[randint(0, 7)], (j, i)) for i in range(num_cols)] for j in range(num_rows)] # i columns, j rows

    return gameMatrix


'''
gameMatrix = init_game_matrix(28, 1)

row_str = ""
matrix_str = ""

for r in range(len(gameMatrix)):
    for c in range(len(gameMatrix[r])):
        row_str += gameMatrix[r][c].__str__()
    matrix_str += row_str + "\n"
    row_str = ""

print(matrix_str)
'''
