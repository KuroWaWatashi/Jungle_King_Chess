import pygame as p_g

# Here we'll specify the dimentions of the window, board & pieces:
# This responsible for the dimentions of the window:
ACTUAL_DISPLAY_WIDTH = 1440
ACTUAL_DISPLAY_HEIGHT = 920
# Board dimentions:
BOARD_WIDTH= 870
BOARD_HEIGHT = 920
# The difference between the board window and the actual game window:
DIFFERENTIAL_SPECIFIED_WIDTH = 150
DIFFERENTIAL_SPECIFIED_HEIGHT = 60
# The actual game board's dimentional width & height:
BOARD_D_WIDTH = 7
BOARD_D_HEIGHT = 9
# The dimentions of each square:
SQ_SIZE_WIDTH = BOARD_WIDTH // BOARD_D_WIDTH
SQ_SIZE_HEIGHT = (BOARD_HEIGHT - DIFFERENTIAL_SPECIFIED_HEIGHT) // BOARD_D_HEIGHT
# Specifying animation speed:
MAX_FPS = 90
# Initialising pygame:
p_g.init()
screen = p_g.display.set_mode((ACTUAL_DISPLAY_WIDTH, ACTUAL_DISPLAY_HEIGHT))
# Initialising the clock module for timing the CPU tick speed:
clock = p_g.time.Clock()