import pygame
from const import *

class Game:

    def __init__(self):
        pass

    # Show methods

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    colour = (234, 235, 200) # light green
                else:
                    colour = (119, 154, 88) # dark green

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, colour, rect)