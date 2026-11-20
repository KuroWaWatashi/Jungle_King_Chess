import os
import sys
import pygame as p_g
from Game_Framework import Display_Configuration as Dis_Config
from Game_Framework import Button_Class

class Menu:
    def __init__(self, current_menu, menu_background_img = None, title_x_pos = 0, title_y_pos = 0, menu_title_img = None, title_img_scaling_x = 0, title_img_scaling_y = 0, menu_title_input_font = "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/Menu_Title_Font/Minecraft_Lowercase_&_Uppercase_Font.ttf", menu_title_input_font_size = 60, menu_title_txt = None):
        self.ACTUAL_DISPLAY_WIDTH = Dis_Config.ACTUAL_DISPLAY_WIDTH
        self.ACTUAL_DISPLAY_HEIGHT = Dis_Config.ACTUAL_DISPLAY_HEIGHT

        self.current_menu = current_menu
        self.background_img = menu_background_img
        self.menu_title_x_pos = title_x_pos
        self.menu_title_y_pos = title_y_pos
        self.menu_title_img = menu_title_img
        self.title_img_scaling_x = title_img_scaling_x
        self.title_img_scaling_y = title_img_scaling_y
        self.menu_title_input_font = menu_title_input_font
        self.menu_title_input_font_size = menu_title_input_font_size
        self.menu_title_txt = menu_title_txt

        self.buttons = []

        self.index_cycle = None
        self.keyboard_cycle = False

    def quitting_event(self, event):
        if event.type == p_g.QUIT:
            p_g.quit()
            sys.exit()

    def arrow_keys_event(self, event):
        if event.type == p_g.KEYDOWN:
            self.keyboard_cycle = True
            if self.index_cycle is None:
                self.index_cycle = 0
            elif event.key == p_g.K_UP:
                self.index_cycle = (self.index_cycle - 1) % len(self.buttons)
            elif event.key == p_g.K_DOWN:
                self.index_cycle = (self.index_cycle + 1) % len(self.buttons)
            elif event.key == p_g.K_RETURN:
                return self.index_cycle
        return None

    def current_menu_info(self):
        p_g.display.set_caption(self.current_menu)

    def menu_background(self, screen):
        if self.background_img:
            background = p_g.transform.scale(p_g.image.load(self.background_img), (self.ACTUAL_DISPLAY_WIDTH, self.ACTUAL_DISPLAY_HEIGHT))
            screen.blit(background, (0, 0))
        else:
            screen.fill((0, 50, 0))

    def menu_title(self, screen):
        if not self.menu_title_img and not self.menu_title_txt:
            return

        if self.menu_title_img:
            title_image = p_g.image.load(self.menu_title_img)
            title_image = p_g.transform.scale(title_image, (self.title_img_scaling_x, self.title_img_scaling_y))
            self.title_rect = title_image.get_rect(center=(self.menu_title_x_pos, self.menu_title_y_pos))
            screen.blit(title_image, self.title_rect)
        else:
            self.menu_title_font = p_g.font.Font(self.menu_title_input_font, self.menu_title_input_font_size)
            self.title_txt = self.menu_title_font.render(self.menu_title_txt, True, (139, 105, 20))
            self.title_txt_rect = self.title_txt.get_rect(center=(self.menu_title_x_pos, self.menu_title_y_pos))
            screen.blit(self.title_txt, self.title_txt_rect)

    def menu_button(self, buttons):
        self.buttons =[]

        for value in buttons:
            if isinstance(value, dict):
                button_value = Button_Class.Button(button_x_pos = value.get("x", 0), button_y_pos = value.get("y", 0), button_img = value.get("img"), button_input_font = value.get("font", "courier"), button_input_font_size = value.get("font_size", 30), button_txt_input = value.get("text", ""))
                self.buttons.append(button_value)

    def render_button_constructor(self, screen):
        mouse_pos = p_g.mouse.get_pos()
        if_mouse = False

        for index, button in enumerate(self.buttons):
            if isinstance(button, Button_Class.Button):
                if button.check_user_input(mouse_pos):
                    self.index_cycle = None
                    self.keyboard_cycle = False
                    if_mouse = True
                    button.user_selection(mouse_pos, is_selected = False)
                elif self.keyboard_cycle and index == self.index_cycle:
                    button.user_selection(mouse_pos, is_selected = True)
                else:
                    button.user_selection(mouse_pos, is_selected = False)

                button.display_button(screen)

        if if_mouse:
            self.keyboard_cycle = False

        if p_g.mouse.get_pressed()[0]:
            for button in self.buttons:
                if button.check_user_input(mouse_pos):
                    return button.text_input

        return None