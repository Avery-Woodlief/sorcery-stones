from renderer import *


display = Renderer()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.redraw_screen()

pygame.quit()

