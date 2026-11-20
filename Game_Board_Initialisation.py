BACKGROUND_BOARD_OBJECTS = {}
BACKGROUND_SQUARE_IMAGE = {}

def draw_board(screen, screen_dimentions, pygame, game_state, board_dimensions, colors, textures, chess_notation):
    """
    Draws the game board dynamically on the screen.
        screen: Pygame screen to draw on.
        game_state: The current state of the board from GameState.
        board_dimensions: Dictionary containing board width, height, and square sizes.
        colors: Dictionary containing color definitions like BLACK, WHITE.
        textures: Dictionary containing paths to the board and board square textures.
    """
    p_g = pygame

    screen.fill(colors["WHITE"])

    actual_display_width = screen_dimentions["ACTUAL_DISPLAY_WIDTH"]
    actual_display_height = screen_dimentions["ACTUAL_DISPLAY_HEIGHT"]

    sq_size_width = board_dimensions["SQ_SIZE_WIDTH"]
    sq_size_height = board_dimensions["SQ_SIZE_HEIGHT"]
    board_width = board_dimensions["BOARD_WIDTH"]
    board_height = board_dimensions["BOARD_HEIGHT"]
    board_pos_width = board_dimensions["DIFFERENTIAL_SPECIFIED_WIDTH"]
    board_pos_height = board_dimensions["DIFFERENTIAL_SPECIFIED_HEIGHT"]

    ranks_to_rows = chess_notation["RANKS_TO_ROWS"]
    rows_to_ranks = chess_notation["ROWS_TO_RANKS"]
    files_to_cols = chess_notation["FILES_TO_COLS"]
    cols_to_files = chess_notation["COLS_TO_FILES"]

    initial_board = game_state.jungle_board

    # Loop through the board and check each piece:
    for row in range(len(initial_board)):  # Track row index:
        for col in range(len(initial_board[row])):  # Track column index:
            square = initial_board[row][col]  # Current square value:
            # Check if the square contains a valid board object:
            if square in textures["board_objects"]:
                BACKGROUND_BOARD_OBJECTS[(row, col)] = p_g.transform.scale(p_g.image.load(textures["board_objects"][square]), (sq_size_width, sq_size_height))
                # Draw the board object:
                screen.blit(BACKGROUND_BOARD_OBJECTS[(row, col)], (col * sq_size_width + board_pos_width, row * sq_size_height + (board_pos_height // 2)))
            else:
                # Place default grass texture for empty squares:
                BACKGROUND_SQUARE_IMAGE[(row, col)] = p_g.transform.scale(p_g.image.load(textures["default"]), (sq_size_width, sq_size_height))
                # Draw the grass textures:
                screen.blit(BACKGROUND_SQUARE_IMAGE[(row, col)], (col * sq_size_width + board_pos_width, row * sq_size_height + (board_pos_height // 2)))

    # Draw grid lines:
    for row in range(len(initial_board) + 1):
        p_g.draw.line(screen, colors["BLACK"], (board_pos_width, (board_pos_height + (row * sq_size_height)) - 30), (board_width + board_pos_width, (board_pos_height + (row * sq_size_height)) - 30), 5)
    for col in range(len(initial_board[0]) + 1):
        p_g.draw.line(screen, colors["BLACK"], (board_pos_width + (col * sq_size_width), (board_pos_height - 30)), (board_pos_width + (col * sq_size_width), (board_pos_height - 95) + board_height), 5)

    # Drawing the chess notation on the board:
    p_g.draw.rect(screen, "Grey", ((board_pos_width - board_pos_height), 0, (board_width + (2 * board_pos_height)), board_pos_height), 3)
    p_g.draw.rect(screen, "Grey", ((board_pos_width + board_width), 0, board_pos_height, actual_display_height), 3)
    p_g.draw.rect(screen, "Grey", ((board_pos_width - board_pos_height), (board_pos_height + board_height), (board_width + (2 * board_pos_height)), board_pos_height), 3)
    p_g.draw.rect(screen, "Grey", ((board_pos_width - board_pos_height), 0, board_pos_height, actual_display_height), 3)