from Game_Framework.Menu_Class import Menu
from Game_Framework.Events_Class import Events

class MainMenu(Menu):
    def __init__(self, screen):
        super().__init__(current_menu = "Main Menu", menu_background_img = "/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Menu_Background_Image/Standard_Menu_Background_Img.jpg", title_x_pos = 730, title_y_pos = 100, menu_title_input_font_size = 90, menu_title_txt = "Main Menu")
        self.buttons = [
            {"x": 730, "y": 300, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 40, "text": "Demo Mode"},
            {"x": 730, "y": 400, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 40, "text": "Single-Player Mode"},
            {"x": 730, "y": 500, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 40, "text": "Multi-Player Mode"},
            {"x": 730, "y": 600, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 40, "text": "Review Matches"},
            {"x": 730, "y": 700, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 40, "text": "Settings"},
            {"x": 730, "y": 800, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 40, "text": "Return"},
            {"x": 730, "y": 900, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 40, "text": "Quit"}
        ]
        self.menu_button(self.buttons)

    def run(self, screen):
        events = Events()
        selected_index = events.run(screen, self)
        return selected_index