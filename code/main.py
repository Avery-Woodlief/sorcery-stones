from renderer import *


display = Renderer()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (event.button == 1):
                #print("left click")
                mouseX, mouseY = pygame.mouse.get_pos()
                cell_from_mouse = display.grid.euclid_to_cell((mouseX, mouseY))

                selected_block = display.grid[cell_from_mouse]
                display.grid.swap_block_with_right_neighbor(selected_block)


    #print(pygame.mouse.get_pos())
    display.redraw_screen()

    pygame.display.flip()

pygame.quit()

