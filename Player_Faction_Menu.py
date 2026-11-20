from Game_Framework.Menu_Class import Menu
from Game_Framework.Events_Class import Events

class FactionMenu(Menu):
    def __init__(self, screen):
        super().__init__(current_menu = "Faction Menu", menu_background_img = "/Users/khronos/PycharmProjects/Jungle_King_Chess/Game_Assets/Menu_Background_Image/Green_Terracotta_Background_Texture.png", title_x_pos = 730, title_y_pos = 100, menu_title_input_font_size = 90, menu_title_txt = "Faction")
        self.buttons = [
            {"x": 630, "y": 500, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 40, "text": "Red"},
            {"x": 850, "y": 500, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 40, "text": "Black"},
            {"x": 730, "y": 700, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 40, "text": "Return"},
            {"x": 730, "y": 900, "font": "/Users/khronos/PycharmProjects/Jungle_King_Chess/static/fonts/Minecraft_Font.ttf", "font_size": 40, "text": "Quit"}
            ]
        self.menu_button(self.buttons)

    def run(self, screen):
        events = Events()
        selected_index = events.run(screen, self)
        return selected_index