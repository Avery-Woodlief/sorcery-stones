import pygame
from match import *


def merge_matches(matching_block_lists):
    consolidated_lists = []
    for MBL in matching_block_lists:
        for e in MBL:
            consolidated_lists.append(e)
    matching_blocks = set(consolidated_lists)
    return list(matching_blocks)

def merge_list(list_, total):
    if (len(list_) >= 3):
        total.append(list_)

def handle_events(event, display):

    if (event.type == pygame.MOUSEBUTTONDOWN):
        if (event.button == 1):
            #print("left click")
            if (pygame.mouse.get_cursor() == display.images["cursor swapper"]):
                mouseX, mouseY = pygame.mouse.get_pos()
                cell_from_mouse = display.grid.euclid_to_cell((mouseX, mouseY))

                selected_block = display.grid[cell_from_mouse]
                display.grid.swap_block_with_right_neighbor(selected_block)

                r1,c1=cell_from_mouse

                to_merge = []

                row_matching_blocks1 = [(r1, c1 + 1)]
                row_matching_blocks2 = [(r1, c1)]
                column_matching_blocks1 = [(r1, c1 + 1)]
                column_matching_blocks2 = [(r1, c1)]

                row_match_query(display.grid, (r1, c1 + 1), row_matching_blocks1)                
                column_match_query(display.grid, (r1, c1 + 1), column_matching_blocks1)
                row_match_query(display.grid, (r1, c1), row_matching_blocks2)
                column_match_query(display.grid, (r1, c1), column_matching_blocks2)

                merge_list(row_matching_blocks1, to_merge)
                merge_list(row_matching_blocks2, to_merge)
                merge_list(column_matching_blocks1, to_merge)
                merge_list(column_matching_blocks2, to_merge)

                display.grid.blocks_to_del = merge_matches(to_merge)
                #print(display.grid.blocks_to_del)
                display.grid.del_blocks()
                display.grid.blocks_to_del = []
                #print("")
