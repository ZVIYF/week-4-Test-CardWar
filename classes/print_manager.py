class PrintManager:


    def print_goodby(self):
        print("Goodbyyyy......")

    
    def print_main_menu(self):
        print("====== CARD WAR ======")
        print("1. Play a game")
        print("2. Exit")


    def print_game_menu(self):
        print("\n====== CARD WAR ======")
        print("1. Play a turn")
        print("2. Finish game\n")


    def print_errors(self, error):
        print(f"Error: {error}")


    def print_turn(self, cards: tuple, turn_state:str, players: tuple):
        print("\n========== TURN ==========")
        print(f"Player: {cards[0]}")
        print(f"Computer: {cards[1]}")
        self.print_winner(turn_state)
        print(players[0], players[1], sep=" | ")
        print("==========================\n")


    def print_winner(self, turn_state: str):
        if turn_state == "draw":
            print("It's a draw!")
        else:
            print(f"{turn_state.title()} won!")


    def print_game_results(self, game:Game):
        print("\n======== GAME RESULTS ========")
        print(game.player, game.computer, sep=" | ")
        self.print_winner(game.winner)
        print("==========================\n")
