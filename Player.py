import random

class Player(object):
    def __init__(self, player_deck, player_name):
        self.player_points = 50
        self.player_deck = player_deck
        self.player_name = player_name
        self.player_card_hand = []
        self.player_card_discard_pile = []

    def get_hand(self):
        for i in range(5):
            card = self.player_deck.draw()
            if card is None:
                break
            self.player_card_hand.append(card)

        return self.player_card_hand

    def add_card_to_discard(self, card_to_add):
        self.player_card_discard_pile.append(card_to_add)

    # Print player stats
    def print_player_data(self):
        print(f" --- {self.player_name} --- ")
        print(f"Points: {self.player_points}")
        print(f"Cards in hand: {len(self.player_card_hand)}")
        print(f"Cards in Discard pile: {len(self.player_card_discard_pile)}")

    def print_points(self):
        print("---------")
        print(f"{self.player_name}")
        print(f"{self.player_points} points")
        print("---------")
        

   # player_card_hand += [c for c in [self.player_deck.draw() for i in range(5)] if c is not None]