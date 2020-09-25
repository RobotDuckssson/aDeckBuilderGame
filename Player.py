import random
import Deck

class Player(object):
    def __init__(self, player_deck, player_name):
        self.player_points = 50
        self.player_deck = player_deck
        self.player_name = player_name
        self.player_card_hand = []
        self.discard_deck = Deck.DiscardPile()

    def get_hand(self):
        for i in range(5):
            card = self.player_deck.draw()
            # If empty handed in draw pile.
            # Shuffle discard pile to draw pile
            if card is None:
                self.player_deck.deck = self.discard_deck.deck
                card = self.player_deck.draw()
                self.discard_deck.deck = []

            self.player_card_hand.append(card)

        return self.player_card_hand

    def add_card_to_discard(self, card_to_add):
        self.discard_deck.add_to_discard(card_to_add)
        

    # Print player stats
    def print_player_data(self):
        print(f" --- {self.player_name} --- ")
        print(f"Points: {self.player_points}")
        print(f"Cards in hand: {len(self.player_card_hand)}")
        print(f"Cards in Discard pile: {len(self.player_card_discard_pile)}")

    def print_points(self):
        print(f"* {self.player_name}, {self.player_points} points")

    def print_player_hand(self):
        print(f"------ {self.player_name} hand ------")
        for cards in self.player_card_hand:
            print(cards.get_card_info())
        print(f"----------------")