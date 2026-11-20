from Game_Framework.Menu_Class import Menu
from Game_Framework.Events_Class import Events

class StartMenu(Menu):
    def __init__(self, screen):
        super().__init__(current_menu = "Start Menu", menu_background_img = "/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Menu_Background_Image/Jungle_King_Chess_Background_Img.jpg", title_x_pos = 730, title_y_pos = 350, menu_title_img = "/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Start_Menu_Logo_&_Window_Icon_Image/Jungle_King_Chess_Logo.png", title_img_scaling_x = 550, title_img_scaling_y = 550)

        self.buttons = [
            {"x": 730, "y": 730, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 50, "text": "Click To Start!"},
            {"x": 730, "y": 900, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 30, "text": "Quit"}
        ]
        self.menu_button(self.buttons)

    def run(self, screen):
        events = Events()
        selected_index = events.run(screen, self)
        return selected_index