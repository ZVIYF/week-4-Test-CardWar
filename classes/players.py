class Player:

    def __init__(self, name:str):
        self.name = name
        self.cards = []


    def show_card(self)-> Card:
        return self.cards.pop(0)


    def has_cards(self)-> Bool:
        return len(self.cards) > 0 


    def __str__(self):
        return f"{self.name.title()} cards: {len(self.cards)}"
    