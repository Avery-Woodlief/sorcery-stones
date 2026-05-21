import pygame
from match import *


def handle_events(event, display):

    if (event.type == pygame.MOUSEBUTTONDOWN):
        if (event.button == 1):
            #print("left click")
            if (pygame.mouse.get_cursor() == display.images["cursor swapper"]):
                mouseX, mouseY = pygame.mouse.get_pos()
                cell_from_mouse = display.grid.euclid_to_cell((mouseX, mouseY))

                #selected_block = display.grid[cell_from_mouse]
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

                

