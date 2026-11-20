"""
This class is responsible for storing the current state of a game. It will also be determining valid moves during a game. It would even keep a move log during the game.
"""

# Creating a class for the state of the game:
class GameState():

    def __init__(self):
        # This board is a 7 x 9 2D list and each element in the list has 2 characters.
        # First character represents colour e.g. "B" = Blue & "R" = Red.
        # Second character represents the animal piece e.g. "M" = Mouse, "C" = Cat, "D" = Dog, "W" = Wolf, "P" = Leopard, "T" = Tiger, "L" = Lion & "E" = Elephant.
        # Other things to note: "--" = Blank space, "Ri" = River, "Tr" = Trap & "Ba" = Base.
        self.jungle_board = [
            ["RL", "--", "Tr", "Ba", "Tr", "--", "RT"],
            ["--", "RD", "--", "Tr", "--", "RC", "--"],
            ["RM", "--", "RP", "--", "RW", "--", "RE"],
            ["--", "Ri", "Ri", "--", "Ri", "Ri", "--"],
            ["--", "Ri", "Ri", "--", "Ri", "Ri", "--"],
            ["--", "Ri", "Ri", "--", "Ri", "Ri", "--"],
            ["BE", "--", "BW", "--", "BP", "--", "BM"],
            ["--", "BC", "--", "Tr", "--", "BD", "--"],
            ["BT", "--", "Tr", "Ba", "Tr", "--", "BL"]
            ]
        self.b_to_move = True
        self.move_log = []

    # Takes a move as a parameter and executes it:
    def movement_making(self, movement):
        self.jungle_board[movement.start_row][movement.start_col] = "--"
        self.jungle_board[movement.end_row][movement.end_col] = movement.animal_piece_moved
        # For being able to undo the previous movement:
        self.move_log.append(movement)
        # For swaping the players:
        self.b_to_move = not self.b_to_move

    # This method will allow the player to undo the last move made:
    def undo_movements(self):
        # This top fuction checks if the list isEmpty() like you would do with a stack, as a value has to be returned, therfore if not assesed, an error value will be returned instead:
        if len(self.move_log) != 0:
            # This pop function retrives the last value placed into a list/stack aka a First-In-Last-Out (FILO) structure:
            movement = self.move_log.pop()
            self.jungle_board[movement.start_row][movement.start_col] = movement.animal_piece_moved
            self.jungle_board[movement.end_row][movement.end_col] = movement.animal_piece_captured
            # Attribute for swaping the player's turn to the last undoed player's turn:
            self.b_to_move = not self.b_to_move

    # This method retrives all valid movements for all animal pieces on the board & is the core movement for the entierty of the game:
    def get_all_possible_movements(self):
        movements = []
        for x in range(len(self.jungle_board)):
            for y in range(len(self.jungle_board[x])):
                turn = self.jungle_board[x][y][0]
                if (turn == 'B' and self.b_to_move) or (turn == 'R' and not self.b_to_move):
                    animal_piece = self.jungle_board[x][y][1]
                    if animal_piece == 'M':
                        self.mouse_movements(x, y, movements)
                    elif animal_piece == 'C':
                        self.cat_movements(x, y, movements)
                    elif animal_piece == 'D':
                        self.dog_movements(x, y, movements)
                    elif animal_piece == 'W':
                        self.wolf_movements(x, y, movements)
                    elif animal_piece == 'P':
                        self.leopard_movements(x, y, movements)
                    elif animal_piece == 'T':
                        self.tiger_movements(x, y, movements)
                    elif animal_piece == 'L':
                        self.lion_movements(x, y, movements)
                    elif animal_piece == 'E':
                        self.elephant_movements(x, y, movements)
        return movements

    """
    Defining a seperate method for all common/basic movements in the "_animal_pieces_basic_movements" method, which allows all pieces to simulate the basic movement within the "GameState" class, which includes being able to move only one step forward, backward, left & right by one step only.
    """

    def get_all_basic_animal_movements(self, x, y, movements):
        # Defining all possible movements in all possible directions as per (row_offset, col_offset):
        standard_direction = [(1,0), (-1,0), (0,1), (0,-1)]
        for d in standard_direction:
            moved_row = x + d[0]
            moved_col = y + d[1]
            # Ensuring the pieces are moving within the boundaries.
            if 0 <= moved_row < len(self.jungle_board) and 0 <= moved_col < len(self.jungle_board[0]):
                move_made_sq = self.jungle_board[moved_row][moved_col]
                current_moving_piece = self.jungle_board[x][y]
                # Special handling for rats: Rats can move to river squares ("Ri")
                if current_moving_piece[1] == 'M':
                    if move_made_sq == "--" or move_made_sq == "Ri" or (move_made_sq[0] != current_moving_piece[0] and move_made_sq not in ["Tr", "Ba"]):
                        movements.append(AnimalPiecesMovement((x, y), (moved_row, moved_col), self.jungle_board))
                    else:
                        # General rule: piece can move to an empty square or capture an opponent's piece (except traps and rivers)
                        if move_made_sq == "--" or (move_made_sq[0] != current_moving_piece[0] and move_made_sq not in ["Tr", "Ba", "Ri"]):
                            movements.append(AnimalPiecesMovement((x, y), (moved_row, moved_col), self.jungle_board))

    """
    Defining all possible mouse movements at row, col and add these movements to the get_all_possible_movements list.
    """

    def mouse_movements(self, x, y, movements):
        pass

    """
    Defining all possible cat movements at row, col and add these movements to the get_all_possible_movements list.
    """

    def cat_movements(self, x, y, movements):
        pass

    """
    Defining all possible dog movements at row, col and add these movements to the get_all_possible_movements list.
    """

    def dog_movements(self, x, y, movements):
        pass

    """
    Defining all possible wolf movements at row, col and add these movements to the get_all_possible_movements list.
    """

    def wolf_movements(self, x, y, movements):
        pass

    """
    Defining all possible leopard movements at row, col and add these movements to the get_all_possible_movements list.
    """

    def leopard_movements(self, x, y, movements):
        pass

    """
    Defining all possible tiger movements at row, col and add these movements to the get_all_possible_movements list.
    """

    def tiger_movements(self, x, y, movements):
        pass

    """
    Defining all possible lion movements at row, col and add these movements to the get_all_possible_movements list.
    """

    def lion_movements(self, x, y, movements):
        pass

    """
    Defining all possible elephant movements at row, col and add these movements to the get_all_possible_movements list.
    """

    def elephant_movements(self, x, y, movements):
        pass

class AnimalPiecesMovement:
    # Maps keys to values:
    # key : value
    ranks_to_rows = {"1":8, "2":7, "3":6, "4":5,
                     "5":4, "6":3, "7":2, "8":1,
                     "9":0}
    rows_to_ranks = {v:k for k, v in ranks_to_rows.items()}
    files_to_cols = {"A":0, "B":1, "C":2, "D":3,
                     "E":4, "F":5, "G":6, "H":7}
    cols_to_files = {v:k for k, v in files_to_cols.items()}

    def __init__(self, start_sq, end_sq, jungle_board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.animal_piece_moved = jungle_board[self.start_row][self.start_col]
        self.animal_piece_captured = jungle_board[self.end_row][self.end_col]
        self.movement_identification = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
        print(self.movement_identification)

    # This overriding the equalls method, "__eq__" method overrides and compares the "get_all_possible_movements" generated and the user's "mouse_click" movements in order to allow the pieces to move, as both the "get_all_possible_movements" object and the "mouse_click" object are two different objects although they essentially have the same values.
    def __eq__(self, other):
        if isinstance(other, AnimalPiecesMovement):
            return self.movement_identification == other.movement_identification
        return False

    def get_jungle_chess_notation(self):
        # To simulate a real chess notation:
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]