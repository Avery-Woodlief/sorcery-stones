import pygame
from match import *
from player import Player
from announcer import Announcer

player = Player("Avery")
announcer = Announcer(player)


def find_all_matches(grid):
    all_matches = set()

    for r in range(MAX_BLOCKS_Y):
        for c in range(MAX_BLOCKS_X):
            cell = (r, c)

            try:
                grid[cell]
            except IndexError:
                continue

            row_matches = [cell]
            row_match_query(grid, cell, row_matches, 1)
            if len(set(row_matches)) >= 3:
                all_matches.update(row_matches)

            col_matches = [cell]
            column_match_query(grid, cell, col_matches, 1)
            if len(set(col_matches)) >= 3:
                all_matches.update(col_matches)

    return list(all_matches)


def execute_matches_until_stable(display, cell=None):
    while True:
        matches = find_all_matches(display.grid)

        if len(matches) == 0:
            break
        player.score += (100*len(matches))
        #print(player.score)
        display.grid.del_blocks(matches)

def handle_events(event, display):

    if (event.type == pygame.MOUSEBUTTONDOWN):
        if (event.button == 1):
            #print("left click")
            if (pygame.mouse.get_cursor() == display.images["cursor swapper"]):
                mouseX, mouseY = pygame.mouse.get_pos()
                cell_from_mouse = display.grid.euclid_to_cell((mouseX, mouseY))
                display.grid.swap_block_with_right_neighbor(cell_from_mouse)
                execute_matches_until_stable(display, cell_from_mouse)
    try:
        if (event.key == pygame.K_ESCAPE):
            return 1
    except (AttributeError):
        return
                

