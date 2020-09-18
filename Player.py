import random

class Player(object):
    def __init__(self, player_deck):
        self.player_points = 50
        self.player_deck = player_deck
        self.player_card_hand = []
        self.player_card_discard_pile = []

    def get_hand(self):
        for i in range(5):
            card = self.player_deck.draw()
            if card is None:
                break
            player_card_hand.append(card)


   # player_card_hand += [c for c in [self.player_deck.draw() for i in range(5)] if c is not None]