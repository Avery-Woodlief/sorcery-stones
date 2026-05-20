# each match_query is executed with seperate matching_blocks lists which get consolidated into one list after all checks.

def row_match_query(matrix, cell, matching_blocks):

    row = cell[0]
    col = cell[1]

    queried = matrix[cell]

    left_neighbor = None
    right_neighbor = None

    if (col - 1 >= 0):
        left_neighbor = matrix[(row, col - 1)]
    

    if (col + 1 < 7):
        right_neighbor = matrix[(row, col + 1)]
    
    
    if ((left_neighbor != None) and (left_neighbor.type == queried.type)): # go to top of the stack of blocks of same type in the column
        if (left_neighbor.cell not in matching_blocks):
            matching_blocks.append(left_neighbor.cell)
            return row_match_query(matrix, left_neighbor.cell, matching_blocks)

    if ((right_neighbor != None) and (right_neighbor.type == queried.type)): # go from top of stack to the bottom of stack
        if (right_neighbor.cell not in matching_blocks):
            matching_blocks.append(right_neighbor.cell)
            return row_match_query(matrix, right_neighbor.cell, matching_blocks)

    if (len(set(matching_blocks)) >= 3): # using set just counts unique positions, hence unique blocks (blocks and positions are 1-1)
        return True
    else:
        return False

def column_match_query(matrix, cell, matching_blocks):
    row = cell[0]
    col = cell[1]

    queried = matrix[cell]
 
    top_neighbor = None
    bottom_neighbor = None

    if (row - 1 >= 0):
        top_neighbor = matrix[(row - 1, col)]
    if (row + 1 < 15):
        bottom_neighbor = matrix[row + 1, col]

    if ((top_neighbor != None) and (top_neighbor.type == queried.type)): # go to far left of "stack"
        if (top_neighbor.cell not in matching_blocks):        
            matching_blocks.append(top_neighbor.cell)
            return column_match_query(matrix, top_neighbor.cell, matching_blocks)

    elif ((bottom_neighbor != None) and (bottom_neighbor.type == queried.type)): # go from far left to far right of the "stack"
        if (bottom_neighbor.cell not in matching_blocks):        
            matching_blocks.append(bottom_neighbor.cell)
            return column_match_query(matrix, bottom_neighbor.cell, matching_blocks)

    else:
        if (len(set(matching_blocks)) >= 3):
            return True
        else:
            return False

