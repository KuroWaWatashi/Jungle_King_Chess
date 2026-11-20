import pygame as p_g
import sys
from Game_Framework import Display_Configuration as Dis_Config
from Menus.Inital_Game_Menu import StartMenu
from Menus.Main_Menu.Main_Game_Menu import MainMenu
# from Menus.Main_Menu.Demo_Mode import DemoMode
from Menus.Main_Menu.Single_Player_Difficulty_Selection_Menu import SinglePlayerDifficultySelectionMenu
from Menus.Main_Menu.Player_Faction_Menu import FactionMenu

screen = Dis_Config.screen

menu_stack = []

def main_initiator():
    start_menu = StartMenu(screen)
    menu_stack.append(start_menu)

    while menu_stack:
        current_menu = menu_stack[-1]
        print(f"Current Menu: {current_menu}")
        selected_option = current_menu.run(screen)

        # If "Quit" was selected:
        if selected_option == "Quit":
            menu_stack.clear()
            return

        # If "Click To Start!" was selected:
        elif selected_option == "Click To Start!":
            if not any(isinstance(menu, MainMenu) for menu in menu_stack):
                menu_stack.append(MainMenu(screen))

        # If "Demo Mode" or "Multi-Player Mode" was selected:
        elif selected_option == "Demo Mode" or selected_option == "Multi-Player Mode":
            menu_stack.append(FactionMenu(screen))

        # If "Single-Player Mode" was selected:
        elif selected_option == "Single-Player Mode":
            menu_stack.append(SinglePlayerDifficultySelectionMenu(screen))

        # If any of the three difficulty options were selected:
        elif selected_option in ["Novice", "Intermediate", "Apex"]:
            menu_stack.append(FactionMenu(screen))

        # If a faction was selected:
        elif selected_option in ["Red", "Black"]:
            pass
            # menu_stack.append(Game(screen, faction=selected_option))

        elif selected_option == "Return":
            if len(menu_stack) > 1:
                menu_stack.pop()

if __name__ == "__main__":
    main_initiator()

def main_initiator():
    start_menu = StartMenu(screen)
    menu_stack.append(start_menu)

    while menu_stack:
        current_menu = menu_stack[-1]  # ✅ Get the top menu
        print(f"Current Menu: {current_menu}")

        selected_option = current_menu.run(screen)

        # ✅ If "Quit" is selected, clear the stack and exit
        if selected_option == "Quit":
            menu_stack.clear()
            return

        # ✅ If "Click To Start!" is selected, transition correctly
        elif selected_option == "Click To Start!":
            if isinstance(current_menu, StartMenu):
                menu_stack.pop()  # ✅ Remove StartMenu from the stack
                menu_stack.append(MainMenu(screen))  # ✅ Go to Main Menu

        # ✅ Handle all other menu transitions correctly
        elif selected_option == "Demo Mode" or selected_option == "Multi-Player Mode":
            menu_stack.append(FactionMenu(screen))

        elif selected_option == "Single-Player Mode":
            menu_stack.append(SinglePlayerDifficultySelectionMenu(screen))

        elif selected_option in ["Novice", "Intermediate", "Apex"]:
            menu_stack.append(FactionMenu(screen))

        elif selected_option in ["Red", "Black"]:
            pass  # Add game initialization here

        elif selected_option == "Return":
            if len(menu_stack) > 1:
                menu_stack.pop()
