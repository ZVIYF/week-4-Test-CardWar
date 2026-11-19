from random import randint
from .cards import Card
from .players import Player


class Game:

    SYMBOLS = {
        "H": "♥",
        "D": "♦",
        "S": "♠",
        "C": "♣"

    }

    NUMS_TO_VALUES = {
        11: "J",
        12: "Q",
        13: "K",
        14: "A"
    }


    def __init__(self, print_manager, input_manager):
        self.deck = []
        self.input_manager = input_manager
        self.print_manager = print_manager
        self.computer = Player("Computer")
        self.player = Player("player")        
        self.create_deck()
        self.shuffle_deck()
        self.deal_cards()
        

    def create_deck(self):
        for symbol in self.SYMBOLS:
            for i in range(2, 15):
                self.deck.append(Card(i, symbol, self.SYMBOLS, self.NUMS_TO_VALUES))


    def shuffle_deck(self):
        for _ in range(1000):
            take_card_index = randint(0, 51)
            same = True
            while same:
                insert_card_index = randint(0, 50)
                if take_card_index != insert_card_index:
                    same = False
            card = self.deck.pop(take_card_index)
            self.deck.insert(randint(0, 49), card)


    def deal_card(self, player_deck: list):
        player_deck.append(self.deck.pop())


    def deal_cards(self):
        while len(self.deck) > 1:
            self.deal_card(self.computer.cards)
            self.deal_card(self.player.cards)


    def play_turn(self):
        self.check_for_winners()
        player_card = self.player.show_card()
        computer_card = self.computer.show_card()
        winner = self.check_turn_winner(player_card, computer_card)
        self.give_card_to_winner(player_card, computer_card, winner)
        self.print_manager.print_turn((player_card, computer_card), winner, (self.player, self.computer))


    def check_turn_winner(self, player:Card, computer:Card):
        if player.value > computer.value:
            return "player"
        if player.value < computer.value:
            return "computer"
        return "draw"


    def give_card_to_winner(self, player_card, computer_card, winner):
        if winner == "draw":
            self.player.cards.append(player_card)
            self.computer.cards.append(computer_card)
        else:
            self.__getattribute__(winner).cards.append(player_card)
            self.__getattribute__(winner).cards.append(computer_card)


    def check_for_winners(self):
        if self.computer.has_cards() and self.player.has_cards():
            return
        raise ValueError("One of the players does not have cards. Closing game.")

    @property
    def winner(self):
        if len(self.player.cards) > len(self.computer.cards):
            return "player"
        if len(self.player.cards) < len(self.computer.cards):
            return "computer"
        return "draw"