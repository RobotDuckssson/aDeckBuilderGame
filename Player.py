import random

class Player:
    
    def __init__(self, player_deck):
        self.player_points = 50
        self.player_deck = player_deck
        self.player_card_hand = []
        self.player_card_discard_pile = []

    @property
    def player_points(self):
        return self.__player_points

    @player_points.setter
    def player_points(self, player_points):
        self.__player_points = player_points

    @property
    def get_hand(self):
        for i in range(5):
            card_to_hand = random.choice(self.player_deck)
            self.player_card_hand.append(card_to_hand)
            self.player_deck.remove(card_to_hand)

        return self.player_card_hand

