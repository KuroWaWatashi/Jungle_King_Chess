import pygame as p_g

class Button():
    def __init__(self, button_x_pos = 0, button_y_pos = 0, button_img = None, button_input_font = "courier", button_input_font_size = 20, button_txt_input = ""):
        self.x_pos = button_x_pos
        self.y_pos = button_y_pos
        self.image = button_img
        self.text_input = button_txt_input
        self.input_font = button_input_font
        self.input_font_size = button_input_font_size

        # If an image is provided, set up the rect; otherwise, don't define it
        if self.image:
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        else:
            self.rect = None  # No rectangle if no image

        if self.input_font == "courier":
            self.title_font = p_g.font.SysFont(self.input_font, self.input_font_size)
        else:
            self.title_font = p_g.font.Font(self.input_font, self.input_font_size)

        self.text = self.title_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def display_button(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_user_input(self, position):
        # Only check for input if a rect exists (i.e., there's an image)
        if self.rect == None:
            initialised_rect = self.text_rect
        else:
            initialised_rect = self.rect

        if initialised_rect and position[0] in range(initialised_rect.left, initialised_rect.right) and position[1] in range(initialised_rect.top, initialised_rect.bottom):
            return True
        return False

    def user_selection(self, position, is_selected = False):
        initialised_rect = self.rect if self.rect else self.text_rect

        if self.rect == None:
            initialised_rect = self.text_rect
        else:
            initialised_rect = self.rect

        if (initialised_rect and position[0] in range(initialised_rect.left, initialised_rect.right) and position[1] in range(initialised_rect.top, initialised_rect.bottom)) or is_selected:
            self.text = self.title_font.render(self.text_input, True, "green")
        else:
            self.text = self.title_font.render(self.text_input, True, "white")