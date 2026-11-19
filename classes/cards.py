class Card:

    
    def __init__(self, card_value, card_symbol, symbols, nums_names_dict):
        self.value = card_value
        self.symbol = card_symbol
        self.symbols = symbols
        self.nums_names_dict = nums_names_dict


    def __str__(self):
        if self.value > 10:
            return f"{self.nums_names_dict[self.value]}{self.symbols[self.symbol]}"
        return f"{self.value}{self.symbols[self.symbol]}"


    def __repr__(self):
        if self.value > 10:
            return f"{self.nums_names_dict[self.value]}{self.symbols[self.symbol]}"
        return f"{self.symbols[self.symbol]} {self.value}"