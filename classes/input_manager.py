class Inputs:
    def __init__(self, validator):
        self.validator = validator


    def get_players_name(self):
        name = input("Enter Player's name: ")
        return name
    

    def get_menu_choice(self, range:int):
        while True:
            user_input = input("Enter your Choice: ")
            try:
                self.validator.is_not_empty(user_input)
                self.validator.is_number(user_input)
                choice = int(user_input)
                self.validator.is_in_range(choice, range)
            except ValueError as error:
                print(f"Error: {error}")
            else:
                return choice