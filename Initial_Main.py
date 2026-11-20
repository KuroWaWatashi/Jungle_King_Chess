"""
This is the main driver file. It will be responsible for handling user input and displaying information for the current game state and objects.
"""

import pygame as p_g
from Game import Game_Engine_Framework

# Here we'll specify the width, height & dimensions of the board & pieces:
ACTUAL_DISPLAY_WIDTH = 1440
ACTUAL_DISPLAY_HEIGHT = 920
BOARD_WIDTH= 870
BOARD_HEIGHT = 920
DIFFERENTIAL_SPECIFIED_WIDTH = 150
DIFFERENTIAL_SPECIFIED_HEIGHT = 60
BOARD_D_WIDTH = 7
BOARD_D_HEIGHT = 9
SQ_SIZE_WIDTH = BOARD_WIDTH // BOARD_D_WIDTH
SQ_SIZE_HEIGHT = (BOARD_HEIGHT - DIFFERENTIAL_SPECIFIED_HEIGHT) // BOARD_D_HEIGHT
# Specifying animation speed:
MAX_FPS = 90
# Creating a global dictionary for the images of the animal pieces:
PIECE_IMAGE = {}

# Loading the window icon:
def window_icon_load():
    window_icon = p_g.image.load("/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Window_Icon_Image/Jungle_King_Chess.jpeg")
    p_g.display.set_icon(window_icon)

# Loading background image:
JUNGLE_BOARD_IMAGE = p_g.transform.scale(p_g.image.load("/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Board_Image/Jungle_Chess_Board.png"), (BOARD_WIDTH, BOARD_HEIGHT - DIFFERENTIAL_SPECIFIED_HEIGHT))

# Initialising the global dictionary of images, expensive operation, hence load once. This will load all the images at once through a for loop:
def animal_pieces_load():
    pieces = ['BM', 'BC', 'BD', 'BW', 'BP', 'BT', 'BL', 'BE', 'RM', 'RC', 'RD', 'RW', 'RP', 'RT', 'RL', 'RE']
    for animal in pieces:
        if animal == "Tr" or animal == "Ba" or animal == "Ri":
            continue
        else:
            PIECE_IMAGE[animal] = p_g.transform.scale(p_g.image.load("/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Animal_Piece_Images/" + animal + ".png"), (SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))

# New function to draw the pieces
def draw_pieces(screen, jungle_board):
    for row in range(BOARD_D_HEIGHT):
        for col in range(BOARD_D_WIDTH):
            piece = jungle_board[row][col]
            if piece == "Tr" or piece == "Ba" or piece == "Ri":
                continue
            if piece != "--":  # Not an empty square
                screen.blit(PIECE_IMAGE[piece], p_g.Rect(col * SQ_SIZE_WIDTH + DIFFERENTIAL_SPECIFIED_WIDTH, row * SQ_SIZE_HEIGHT + (DIFFERENTIAL_SPECIFIED_HEIGHT // 2), SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))

"""
This is the main driver of our code, which will handle all the user input and updating the graphics.
"""

def main_display_driver():
    p_g.init()
    screen = p_g.display.set_mode((ACTUAL_DISPLAY_WIDTH, ACTUAL_DISPLAY_HEIGHT))
    # Initialising the clock module for timing the CPU tick speed:
    clock = p_g.time.Clock()
    g_s = Game_Engine.GameState()
    valid_movements = g_s.get_all_possible_movements()
    # Setting a flag variable for when a move is made:
    movement_made = False
    window_icon_load()
    p_g.display.set_caption("Jungle King Chess")
    animal_pieces_load()

    running = True
    # An empty (tuple: (row, col)) that keep tracks of the player's last registered square clicked:
    sq_selected = ()
    # This empty list keeps track of the player's clicks with two tuples ([(x, y), (x, y)]):
    player_click = []
    while running:
        for event in p_g.event.get():
            if event.type == p_g.QUIT:
                running = False
            # Mouse handling section of the code:
            elif event.type == p_g.MOUSEBUTTONDOWN:
                mouse_location = p_g.mouse.get_pos()
                # col = x, row = y, this retrives the location of the user click that allows the pieces to move horizontally or vertically:
                col = (mouse_location[0] - DIFFERENTIAL_SPECIFIED_WIDTH) // SQ_SIZE_WIDTH
                row = (mouse_location[1] - (DIFFERENTIAL_SPECIFIED_HEIGHT // 2)) // SQ_SIZE_HEIGHT
                # This will determine whether the user clicks the same square twice:
                if sq_selected == (row, col):
                    # Deselects:
                    sq_select = ()
                    # Clear player clicks:
                    player_click = []
                else:
                    sq_select = (row, col)
                    # This will append for both 1st & 2nd clicks:
                    player_click.append(sq_select)
                # After the second click:
                if len(player_click) == 2:
                    movement = Game_Engine.RegisteredPieceMovement(player_click[0], player_click[1], g_s.jungle_board)
                    print(movement.get_jungle_chess_notation())
                    if movement in valid_movements:
                        g_s.movement_making(movement)
                        movement_made = True
                    # Resets the user's clicks:
                    sq_selected = ()
                    player_click = []
            # This Pygame event will undo the player's last move when the 'z' key is pressed:
            elif event.type == p_g.KEYDOWN:
                # Undo's the last movement of the user when the 'z' key is pressed:
                if event.key == p_g.K_z:
                    g_s.undo_movements()
                    movement_made = True

        if movement_made:
            valid_movements = g_s.get_all_possible_movements()
            movement_made = False

        screen.fill("black")
        screen.blit(JUNGLE_BOARD_IMAGE, (DIFFERENTIAL_SPECIFIED_WIDTH, DIFFERENTIAL_SPECIFIED_HEIGHT // 2))
        draw_pieces(screen, g_s.jungle_board)
        clock.tick(MAX_FPS)
        p_g.display.flip()

if __name__ == "__main__":
    main_display_driver()