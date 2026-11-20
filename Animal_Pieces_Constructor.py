class AnimalPiecesConstructor:
    Animal_Pieces_Info = {}
    Animal_Pieces = {}

    def __init__(self, screen, pygame, game_state, board_dimensions):
        self.screen = screen
        self.p_g = pygame
        self.sq_size_width = board_dimensions["SQ_SIZE_WIDTH"]
        self.sq_size_height = board_dimensions["SQ_SIZE_HEIGHT"]
        self.board_pos_width = board_dimensions["DIFFERENTIAL_SPECIFIED_WIDTH"]
        self.board_pos_height = board_dimensions["DIFFERENTIAL_SPECIFIED_HEIGHT"]
        self.initial_board = game_state.jungle_board
        self.center = (self.sq_size_width // 2, self.sq_size_height // 2)
        self.sq_size_boundry_for_piece_img = min(self.sq_size_width, self.sq_size_height) - 70

        self.animal_names = ["M", "C", "D", "W", "P", "T", "L", "E"]

        self.FACTION_COLOURS = {"R": (255, 0, 0), "B": (0, 0, 0)}
        self.TEXT_FONT_SIZE = 40
        self.PIECE_FONT_COLOUR = (255, 255, 255)

    def animal_dict_constructor(self):
        animal_ranks = [1, 2, 3, 4, 5, 6, 7, 8]

        for index in range(len(self.animal_names)):
            animal_type = self.animal_names[index]

            animal_img_path = f"/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Animal_Piece_Image/{animal_type}.png"
            scaled_img = self.p_g.transform.scale(self.p_g.image.load(animal_img_path).convert_alpha(), (self.sq_size_boundry_for_piece_img + 35, self.sq_size_boundry_for_piece_img + 40))

            AnimalPiecesConstructor.Animal_Pieces_Info[self.animal_names[index]] = {"Rank": animal_ranks[index], "Image_Path": scaled_img}

    def construct_animal_piece_background(self):
        for row in range(len(self.initial_board)):
            for col in range(len(self.initial_board[row])):
                square = self.initial_board[row][col]
                if square[1] in self.animal_names:
                    faction = square[0]

                    piece_img_background_surface = self.p_g.Surface((self.sq_size_width, self.sq_size_height), self.p_g.SRCALPHA)
                    self.p_g.draw.circle(piece_img_background_surface, self.FACTION_COLOURS[faction], self.center, (self.sq_size_width // 2) - 15)
                    image = AnimalPiecesConstructor.Animal_Pieces_Info[square[1]]["Image_Path"]
                    blit_x_pos = (self.sq_size_width // 2 - image.get_width() // 2) - 15
                    blit_y_pos = self.sq_size_height // 2 - image.get_height() // 2
                    piece_img_background_surface.blit(image, (blit_x_pos, blit_y_pos))

                    rank = AnimalPiecesConstructor.Animal_Pieces_Info[square[1]]["Rank"]
                    font = self.p_g.font.SysFont("Courier New", self.TEXT_FONT_SIZE)
                    rank_text = font.render(str(rank), True, self.PIECE_FONT_COLOUR)
                    text_x_pos = ((self.sq_size_width // 2) - (rank_text.get_width() // 2)) + 28
                    text_y_pos = self.sq_size_height - 50
                    piece_img_background_surface.blit(rank_text, (text_x_pos, text_y_pos))

                    AnimalPiecesConstructor.Animal_Pieces[(row, col)] = piece_img_background_surface

    @staticmethod
    def animal_piece_updater(screen, board_dimensions, jungle_board, animal_pieces):
        board_d_width = len(jungle_board)
        board_d_height = len(jungle_board[0])

        sq_size_width = board_dimensions["SQ_SIZE_WIDTH"]
        sq_size_height = board_dimensions["SQ_SIZE_HEIGHT"]
        board_pos_width = board_dimensions["DIFFERENTIAL_SPECIFIED_WIDTH"]
        board_pos_height = board_dimensions["DIFFERENTIAL_SPECIFIED_HEIGHT"]

        for row in range(board_d_width):
            for col in range(board_d_height):
                piece = jungle_board[row][col]
                if piece in ["Tr", "Ba", "Ri"]:
                    continue
                if piece != "--":
                    screen.blit(animal_pieces[(row, col)], (col * sq_size_width + board_pos_width, row * sq_size_height + (board_pos_height // 2)))