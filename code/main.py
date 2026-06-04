from renderer import *
from event_handler import *
from game_exceptions import GameOver
from math import sqrt


display = Renderer()

def inside_quit_circle(mouse_pos):
    mouse_x, mouse_y = mouse_pos
    return sqrt((mouse_x - 1053)**2 + (mouse_y - 780)**2) <= 31



running = True
while running:
    
    execute_matches_until_stable(display)
    for event in pygame.event.get():
        
        '''
        try:
            print(event.pos)
        except (AttributeError):
            continue
        '''
        
        if (event.type == pygame.MOUSEBUTTONDOWN):
            mouse_pos = event.pos
            if (inside_quit_circle(mouse_pos)):
                running = False
        
        if event.type == pygame.QUIT:
            running = False
        if (handle_events(event, display) == 1):
            running = False

    try:
        display.redraw_screen()
    except (GameOver):
        running = False
    #pygame.display.flip()

pygame.quit()
