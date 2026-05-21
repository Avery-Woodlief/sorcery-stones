import pygame
from match import *


def execute_matches_until_stable(display, cell):
    r1, c1 = cell
    r1_stable = False
    r2_stable = False
    c1_stable = False
    c2_stable = False

    while (not (r1_stable and r2_stable and c1_stable and c2_stable)):

        try:
            row_matching_blocks = [(r1, c1 + 1)]
            row_match_query(display.grid, (r1, c1 + 1), row_matching_blocks, 1)
            if (len(list(set(row_matching_blocks))) >= 3):
                display.grid.del_blocks(list(set(row_matching_blocks)))
                r1_stable = False
            else:
                r1_stable = True
        except:
            r1_stable = True

    
        try:
            row_matching_blocks = [(r1, c1)]
            row_match_query(display.grid, (r1, c1), row_matching_blocks, 1)
            if (len(list(set(row_matching_blocks))) >= 3):
                display.grid.del_blocks(list(set(row_matching_blocks)))
                r2_stable = False
            else:
                r2_stable = True
        except:
            r2_stable = True

        try:
            col_matching_blocks = [(r1, c1 + 1)]
            column_match_query(display.grid, (r1, c1 + 1), col_matching_blocks, 1)
            if (len(list(set(col_matching_blocks))) >= 3):
                display.grid.del_blocks(list(set(col_matching_blocks)))
                c1_stable = False
            else:
                c1_stable = True
        except:
            c1_stable = True

        try:
            col_matching_blocks = [(r1, c1)]
            column_match_query(display.grid, (r1, c1), col_matching_blocks, 1)
            if (len(list(set(col_matching_blocks))) >= 3):
                display.grid.del_blocks(list(set(col_matching_blocks)))
                c2_stable = False
            else:
                c2_stable = True
        except:
            c2_stable = True

def handle_events(event, display):

    if (event.type == pygame.MOUSEBUTTONDOWN):
        if (event.button == 1):
            #print("left click")
            if (pygame.mouse.get_cursor() == display.images["cursor swapper"]):
                mouseX, mouseY = pygame.mouse.get_pos()
                cell_from_mouse = display.grid.euclid_to_cell((mouseX, mouseY))
                display.grid.swap_block_with_right_neighbor(cell_from_mouse)
                execute_matches_until_stable(display, cell_from_mouse)
                #selected_block = display.grid[cell_from_mouse]
                '''
                try:
                    display.grid.swap_block_with_right_neighbor(cell_from_mouse)
                    r1,c1=cell_from_mouse

                    row_matching_blocks = [(r1, c1 + 1)]
                    row_match_query(display.grid, (r1, c1 + 1), row_matching_blocks, 1)
                    if (len(list(set(row_matching_blocks))) >= 3):
                        display.grid.del_blocks(list(set(row_matching_blocks)))

                    row_matching_blocks = [(r1, c1)]
                    row_match_query(display.grid, (r1, c1), row_matching_blocks, 1)
                    if (len(list(set(row_matching_blocks))) >= 3):
                        display.grid.del_blocks(list(set(row_matching_blocks)))

                    col_matching_blocks = [(r1, c1 + 1)]
                    column_match_query(display.grid, (r1, c1 + 1), col_matching_blocks, 1)
                    if (len(list(set(col_matching_blocks))) >= 3):
                        display.grid.del_blocks(list(set(col_matching_blocks)))

                    col_matching_blocks = [(r1, c1)]
                    column_match_query(display.grid, (r1, c1), col_matching_blocks, 1)
                    if (len(list(set(col_matching_blocks))) >= 3):
                        display.grid.del_blocks(list(set(col_matching_blocks)))

                
                except (ValueError) as e:
                    return # nothing to do
                '''

                

