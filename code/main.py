from renderer import *
from event_handler import *



display = Renderer()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (handle_events(event, display) == 1):
            running = False

    display.redraw_screen()
    #pygame.display.flip()

pygame.quit()
