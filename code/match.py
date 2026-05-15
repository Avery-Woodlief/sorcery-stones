# each match_query is executed with seperate matching_blocks lists which get consolidated into one list after all checks.

def column_match_query(matrix, pos, matching_blocks):

    
    

    row = pos[0]
    col = pos[1]

    queried = matrix[row][col]

    left_neighbor = None
    right_neighbor = None

    if (col - 1 >= 0):
        left_neighbor = matrix[row][col - 1]
    

    if (col + 1 < 7):
        right_neighbor = matrix[row][col + 1]
    
    
    if ((left_neighbor != None) and (left_neighbor.type == queried.type)): # go to top of the stack of blocks of same type in the column
        if (left_neighbor.pos not in matching_blocks):
            matching_blocks.append(left_neighbor.pos)
            return column_match_query(matrix, left_neighbor.pos, matching_blocks)

    if ((right_neighbor != None) and (right_neighbor.type == queried.type)): # go from top of stack to the bottom of stack
        if (right_neighbor.pos not in matching_blocks):
            matching_blocks.append(right_neighbor.pos)
            return column_match_query(matrix, right_neighbor.pos, matching_blocks)

    if (len(set(matching_blocks)) >= 3): # using set just counts unique positions, hence unique blocks (blocks and positions are 1-1)
        return True
    else:
        return False

def row_match_query(matrix, pos, matching_blocks):
    row = pos[0]
    col = pos[1]

    queried = matrix[row][col]
 
    top_neighbor = None
    bottom_neighbor = None

    if (row - 1 >= 0):
        top_neighbor = matrix[row - 1][col]
    if (row + 1 < 28)
        bottom_neighbor = matrix[row + 1][col]

    if ((top_neighbor != None) and (top_neighbor.type == queried.type)): # go to far left of "stack"
        if (top_neighbor.pos not in matching_blocks):        
            matching_blocks.append(top_neighbor.pos)
            return row_match_query(matrix, top_neighbor.pos, matching_blocks)

    elif ((bottom_neighbor != None) and (bottom_neighbor.type == queried.type)): # go from far left to far right of the "stack"
        if (bottom_neighbor.pos not in matching_blocks):        
            matching_blocks.append(bottom_neighbor.pos)
            return row_match_query(matrix, bottom_neighbor.pos, matching_blocks)

    else:
        if (len(set(matching_blocks)) >= 3):
            return True
        else:
            return False

