from game_matrix import *
import pygame
import re

class Renderer:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
        self.template = pygame.image.load("../media/images/template.png")
        #self.background = pygame.image.load("../media/images/black_rect.png")
        self.grid = Grid() # initial grid of blocks
        
        self.clock = pygame.time.Clock()

        CURSOR_SWAPPER = pygame.cursors.Cursor((BLOCK_WIDTH//2 - 1, BLOCK_HEIGHT//2 - 1), # middle of left block to swap
                                                pygame.image.load("../media/images/cursor.png").convert_alpha())
        wand = pygame.image.load("../media/images/wand.png").convert_alpha()
        wand = pygame.transform.scale(wand, (50, 50))
        WAND_CURSOR = pygame.cursors.Cursor((0, 0), wand)
        LASER_POINTER = pygame.image.load("../media/images/pointer.png")

        self.images = {"cursor swapper":CURSOR_SWAPPER, "laser pointer":LASER_POINTER, "wand cursor":WAND_CURSOR}

        

        SCORE_NUMS = [pygame.transform.scale(pygame.image.load(f"../media/images/score nums/{i}.png").convert_alpha(), (31, 75)) for i in range(10)]
        self.score_nums = {f'{i}':SCORE_NUMS[i] for i in range(10)}

        BLOCKS_LEFT_NUMS = [pygame.transform.scale(pygame.image.load(f"../media/images/small nums/{i}.png").convert_alpha(), (22, 30)) for i in range(10)]
        self.blocks_left_nums = {f'{i}':BLOCKS_LEFT_NUMS[i] for i in range(10)}
        
        LEVEL_NUMS = [pygame.transform.scale(pygame.image.load(f"../media/images/level nums/{i}.png").convert_alpha(), (65, 47)) for i in range(1, 5)]
        self.level_nums = {i:LEVEL_NUMS[i - 1] for i in range(1, 5)}

    def update_and_show_blocks_left(self):
        blocks_left = self.grid.level_conditions[self.grid.level] - self.grid.blocks_matched_counter
        placements = 2
        digits = re.findall(r"\d", str(blocks_left))
        leading_zeros = placements - len(digits)
        for i in range(leading_zeros):
            digits.insert(0, '0')
        start_x = 994
        start_y = 663
        card_width = 22
        i = 0 # the 0th digit
        for digit in digits:
            self.screen.blit(self.blocks_left_nums[digit], (start_x + (i * card_width), start_y))
            i += 1

    def update_and_show_current_level(self):
        self.grid.check_level_condition()
        current_level = self.grid.level
        x = 252
        y = 715
        self.screen.blit(self.level_nums[current_level], (x, y))

    def update_and_show_player_score(self):
        player_score = self.grid.player.score
        placements = 8
        digits = re.findall(r"\d", str(player_score))
        leading_zeros = placements - len(digits)
        for i in range(leading_zeros):
            digits.insert(0, '0')
        start_x = 46
        start_y = 621
        card_width = 31
        card_height = 75
        barrier_size = 4
        i = 0 # the 0th digit
        for digit in digits:
            self.screen.blit(self.score_nums[digit], (start_x + (i * barrier_size) + (i * card_width), start_y))
            i += 1

    def draw_blocks(self):
        
        for block in self.grid.block_list:
            pos = self.grid.cell_to_euclid(block.cell)
            self.screen.blit(block.img, pos)
    
    def redraw_screen(self):
        
        self.screen.fill(COLOR_BLACK)
        self.screen.blit(self.template, (0, 0))
        self.update_and_show_blocks_left()
        self.update_and_show_current_level()
        self.update_and_show_player_score()
        self.draw_blocks()
        self.grid.raise_up()
        self.grid.check_lose_condition()
        
        #self.grid.move_blocks_up(30)
        mouseX, mouseY = pygame.mouse.get_pos()
        

        cell_found = self.grid.euclid_to_cell((mouseX, mouseY))
        if (cell_found[0] < 0):
            pygame.mouse.set_cursor(self.images["wand cursor"])
        else:
            pygame.mouse.set_cursor(self.images["cursor swapper"])
            self.screen.blit(self.images["laser pointer"], (mouseX, mouseY))
        pygame.display.flip()
        self.clock.tick(60)

