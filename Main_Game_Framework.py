import pygame as p_g
from Game_Framework import Display_Configuration as Dis_Config
from Game_Framework.Game_Board_Initialisation import draw_board
from Game import Game_Engine_Framework
from Game_Framework.Animal_Pieces_Constructor import AnimalPiecesConstructor

# Here we'll specify the dimentions of the window, board & pieces:
# This responsible for the dimentions of the window:
ACTUAL_DISPLAY_WIDTH = Dis_Config.ACTUAL_DISPLAY_WIDTH
ACTUAL_DISPLAY_HEIGHT = Dis_Config.ACTUAL_DISPLAY_HEIGHT
# Board dimentions:
BOARD_WIDTH = Dis_Config.BOARD_WIDTH
BOARD_HEIGHT = Dis_Config.BOARD_HEIGHT
# The difference between the board window and the actual game window:
DIFFERENTIAL_SPECIFIED_WIDTH = Dis_Config.DIFFERENTIAL_SPECIFIED_WIDTH
DIFFERENTIAL_SPECIFIED_HEIGHT = Dis_Config.DIFFERENTIAL_SPECIFIED_HEIGHT
# The actual game board's dimentional width & height:
BOARD_D_WIDTH = Dis_Config.BOARD_D_WIDTH
BOARD_D_HEIGHT = Dis_Config.BOARD_D_HEIGHT
# The dimentions of each square:
SQ_SIZE_WIDTH = Dis_Config.SQ_SIZE_WIDTH
SQ_SIZE_HEIGHT = Dis_Config.SQ_SIZE_HEIGHT
# Specifying animation speed:
MAX_FPS = Dis_Config.MAX_FPS
screen = Dis_Config.screen
# Initialising the clock module for timing the CPU tick speed:
clock = Dis_Config.clock
# Initialising the chess notation for representation on screen:
RANKS_TO_ROWS = Game_Engine_Framework.RegisteredPieceMovement.ranks_to_rows
ROWS_TO_RANKS = Game_Engine_Framework.RegisteredPieceMovement.rows_to_ranks
FILES_TO_COLS = Game_Engine_Framework.RegisteredPieceMovement.files_to_cols
COLS_TO_FILES = Game_Engine_Framework.RegisteredPieceMovement.cols_to_files

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Board dimensions dictionary
board_dimensions = {
    "BOARD_WIDTH": BOARD_WIDTH,
    "BOARD_HEIGHT": BOARD_HEIGHT,
    "SQ_SIZE_WIDTH": SQ_SIZE_WIDTH,
    "SQ_SIZE_HEIGHT": SQ_SIZE_HEIGHT,
    "DIFFERENTIAL_SPECIFIED_WIDTH": DIFFERENTIAL_SPECIFIED_WIDTH,
    "DIFFERENTIAL_SPECIFIED_HEIGHT": DIFFERENTIAL_SPECIFIED_HEIGHT
}

# Textures dictionary
textures = {
    "board_objects": {
        "Ri": "/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Board_Object_Images/Ri.png",
        "Tr": "/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Board_Object_Images/Tr.png",
        "Ba": "/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Board_Object_Images/Ba.png"
    },
    "default": "/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Board_Object_Images/Grass_Block_(Top_Texture)_Image.png"
}

# Colors dictionary
colors = {
    "BLACK": BLACK,
    "WHITE": WHITE
}

chess_notation = {
    "RANKS_TO_ROWS": RANKS_TO_ROWS,
    "ROWS_TO_RANKS": ROWS_TO_RANKS,
    "FILES_TO_COLS": FILES_TO_COLS,
    "COLS_TO_FILES": COLS_TO_FILES
}

screen_dimentions = {
    "ACTUAL_DISPLAY_WIDTH": ACTUAL_DISPLAY_WIDTH,
    "ACTUAL_DISPLAY_HEIGHT": ACTUAL_DISPLAY_HEIGHT
}

# Loading the window icon:
def window_icon_load():
    window_icon = p_g.image.load("/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Start_Menu_Logo_&_Window_Icon_Image/Jungle_King_Chess_Logo.png")
    p_g.display.set_icon(window_icon)

"""
This is the main driver of our code, which will handle all the user input and updating the graphics.
"""

def main_display_driver():
    # Initializing pygame
    p_g.init()

    # Initializing the game state
    g_s = Game_Engine_Framework.GameState()
    valid_movements = g_s.get_all_possible_movements()

    movement_made = False
    sq_selected = ()
    player_clicks = []

    window_icon_load()
    p_g.display.set_caption("Jungle King Chess")

    # Initializing Animal Pieces
    animal_pieces = AnimalPiecesConstructor(screen, p_g, g_s, board_dimensions)
    animal_pieces.animal_dict_constructor()
    animal_pieces.construct_animal_piece_background()

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
                if len(player_click) == 1:
                    possible_sq_moves = Game_Engine_Framework.AnimalPiecesMovement
                # After the second click:
                elif len(player_click) == 2:
                    movement = Game_Engine_Framework.RegisteredPieceMovement(player_click[0], player_click[1], g_s.jungle_board)
                    print(movement.get_jungle_chess_notation())
                    if movement in valid_movements:
                        g_s.movement_making(movement)
                        movement_made = True
                    # Resets the user's clicks:
                    sq_selected = ()
                    player_click = []

        if movement_made:
            valid_movements = g_s.get_all_possible_movements()
            movement_made = False
            animal_pieces.construct_animal_piece_background()

        screen.fill("White")
        draw_board(screen, screen_dimentions, p_g, g_s, board_dimensions, colors, textures, chess_notation)
        AnimalPiecesConstructor.animal_piece_updater(screen, board_dimensions, g_s.jungle_board, AnimalPiecesConstructor.Animal_Pieces)
        clock.tick(MAX_FPS)
        p_g.display.flip()

if __name__ == "__main__":
    main_display_driver()