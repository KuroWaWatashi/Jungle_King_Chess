class FactionDetermined:
    def __init__(self, player_mode, player_selection):
        self.player_mode = player_mode
        self.player_selection = player_selection
        if self.player_mode in ["Novice", "Intermediate", "Apex"]:
            self.get_faction_for_single_player()

    def get_faction_for_single_player(self):
        if player_selection == "Red":
            return player_selection
        else:
            return player_selection

    def get_faction_for_multi_player(self, player_selection):
        if self.