from .validations import Validator
from .print_manager import PrintManager
from .input_manager import Inputs
from .game_manager import Game


class MenuManager:
    def __init__(self):
        self.validator = Validator()
        self.ipnut_manager = Inputs(self.validator)
        self.print_manager = PrintManager()



    def run(self):
        self.main_menu()


    def main_menu(self):
        exit = False
        while not exit:
            self.print_manager.print_main_menu()
            choice = self.ipnut_manager.get_menu_choice(2)
            match choice:
                case 1:
                    self.new_game()
                case 2:
                    exit = True
        self.print_manager.print_goodby()


    def new_game(self):
        game = Game(self.print_manager, self.ipnut_manager)
        play_is_on = True
        while play_is_on:
            self.print_manager.print_game_menu()
            choice = self.ipnut_manager.get_menu_choice(2)
            match choice:
                case 1:
                    try:
                        game.play_turn()
                    except ValueError as error:
                        self.print_manager.print_errors(error)
                        play_is_on = False 
                case 2:
                    play_is_on = False
        self.print_manager.print_game_results(game)