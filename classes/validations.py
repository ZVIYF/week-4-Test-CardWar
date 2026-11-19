class Validator:

    def is_not_empty(self, string:str):
        if not string:
            raise ValueError("Please type anything!")


    def is_number(self, string:str):
        if not string.isdigit():
            raise ValueError("Must be a number!")


    def is_in_range(self, number, range):
        if (number < 1) or (number > range):
            raise ValueError(f"Number must be in range 1 - {range}!")