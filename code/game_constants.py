PYGAME_TOP_BAR_HEIGHT = 37 # in pixels
TEMPLATE_OFFSET_Y = 12 # in pixels
BLOCK_SPACING_X = 0.45 # in pixels
BLOCK_SPACING_Y = 0 # in pixels
BLOCK_WIDTH = 50 # in pixels
BLOCK_HEIGHT = 50 # in pixels
SCREEN_WIDTH = 1182 # in pixels
SCREEN_HEIGHT = 877 # in pixels
MAX_BLOCKS_X = 7 # in blocks
MAX_BLOCKS_Y = 15 # in blocks

COLOR_BLACK = (0, 0, 0) # in rgb
COLOR_WHITE = (255, 255, 255) # in rgb

COLUMN_RANGES = {i:(385 + (i * (50 + BLOCK_SPACING_X)),
                    435 + (i * (50 + BLOCK_SPACING_X))) for i in range(MAX_BLOCKS_X)}

ROW_RANGES = {j:(805-PYGAME_TOP_BAR_HEIGHT-TEMPLATE_OFFSET_Y - j * (50 + BLOCK_SPACING_Y), 
                 855-PYGAME_TOP_BAR_HEIGHT-TEMPLATE_OFFSET_Y - j * (50 + BLOCK_SPACING_Y)) for j in range(MAX_BLOCKS_Y)}





