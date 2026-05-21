from game_constants import *

# each match_query is executed with seperate matching_blocks lists which get consolidated into one list after all checks.

def row_match_query(grid, cell, matching_blocks, direction):

    '''
    direction: 1 means go left, 0 means go right, -1 is when both are exhausted
    duplicates are handled elsewhere
    '''

    if (direction == -1):
        return

    row, col = cell
    queried = grid[cell]

    if (direction == 1):
        if (col - 1 < 0): # no left neighbor
            return row_match_query(grid, cell, matching_blocks, direction=0) # now go right
        elif (col - 1 >= 0):
            # left neighbor exists, so grab it, check it, continue
            left_cell = (row, col - 1)
            left = grid[left_cell]
            if (left.type == queried.type):
                matching_blocks.append(left_cell)
                return row_match_query(grid, left_cell, matching_blocks, direction=1) # match found so keep going left
            else:
                return row_match_query(grid, cell, matching_blocks, direction=0) # now go right
                    # using cell instead of left_cell here avoids more duplicates
    elif (direction == 0):
        if (col + 1 >= MAX_BLOCKS_X): # no right neighbor
            return row_match_query(grid, cell, matching_blocks, direction=-1)
        elif (col + 1 < MAX_BLOCKS_X):
            # right neighbor exists, so grab it, check it, continue
            right_cell = (row, col + 1)
            right = grid[right_cell]
            if (right.type == queried.type):
                matching_blocks.append(right_cell)
                # NOTE: using cell instead of right_cell in recall = infinite loop going between same two blocks
                return row_match_query(grid, right_cell, matching_blocks, direction=0) # keep going right
            else:
                return row_match_query(grid, cell, matching_blocks, direction=-1)

def column_match_query(grid, cell, matching_blocks, direction):
    
    '''
    direction: 1 means go up, 0 means go down, -1 is when both are exhausted
    duplicates are handled elsewhere
    '''

   
    if (direction == -1):
        return 

    row, col = cell
    queried = grid[cell]

    if (direction == 1):
        if (row + 1 >= MAX_BLOCKS_Y): # no top neighbor
            return column_match_query(grid, cell, matching_blocks, direction=0) # now go downwards
        elif (row + 1 < MAX_BLOCKS_Y): # top neighbor exists
            # grabbing top neighbor from grid
            top_cell = (row + 1, col)
            top = grid[top_cell]
            if (top.type == queried.type):
                matching_blocks.append(top_cell) # put in here if top is same type as queried
                return column_match_query(grid, top_cell, matching_blocks, direction=1) # keep going up
            else:
                return column_match_query(grid, cell, matching_blocks, direction = 0) # top neighbor is not same type, now start going down

    if (direction == 0):
        if (row - 1 < 0): # no bottom neighbor
            return column_match_query(grid, cell, matching_blocks, direction=-1) # end the search entirely
        elif (row - 1 >= 0): 
            # bottom neighbor exists, so grab it, check it, continue
            bot_cell = (row - 1, col)
            bot = grid[bot_cell]
            if (bot.type == queried.type):
                matching_blocks.append(bot_cell)
                return column_match_query(grid, bot_cell, matching_blocks, direction=0)
            else: # bottom neighbor is different type
                return column_match_query(grid, cell, matching_blocks, direction=-1)




