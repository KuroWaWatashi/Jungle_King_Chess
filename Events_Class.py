import pygame as p_g

class Events:
    def run(self, screen, current_menu):
        while True:
            current_menu.current_menu_info()
            current_menu.menu_background(screen)
            current_menu.menu_title(screen)

            selected_button = None

            for event in p_g.event.get():
                current_menu.quitting_event(event)

                if event.type == p_g.KEYDOWN:
                    if event.key == p_g.K_ESCAPE:
                        return "Quit"

                arrow_selection = current_menu.arrow_keys_event(event)
                if arrow_selection is not None:
                    return current_menu.buttons[arrow_selection].text_input

                if event.type == p_g.MOUSEBUTTONDOWN:
                    selected_button = current_menu.render_button_constructor(screen)

            current_menu.render_button_constructor(screen)
            p_g.display.update()

            if selected_button is not None:
                return selected_button