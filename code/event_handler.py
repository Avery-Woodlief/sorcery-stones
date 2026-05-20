import pygame

def handle_events(event, display):

    if (event.type == pygame.MOUSEBUTTONDOWN):
        if (event.button == 1):
            #print("left click")
            if (pygame.mouse.get_cursor() == display.images["cursor swapper"]):
                mouseX, mouseY = pygame.mouse.get_pos()
                cell_from_mouse = display.grid.euclid_to_cell((mouseX, mouseY))

                selected_block = display.grid[cell_from_mouse]
                display.grid.swap_block_with_right_neighbor(selected_block)
