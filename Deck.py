import random
from Card import Card

class Deck(object):
    def __iter__(self):
        return iter(self.deck)

    def shuffle(self):
        #random doesnt return anything :')
        random.shuffle(self.deck)

    def draw(self):
        try:
            return self.deck.pop()
        except IndexError:
            return None


class ExplorerDeck(Deck):
    def __init__(self):
        deck = []
        for i in range(10):
            deck.append(Card("Unaligned", "Explorer", "Ship", "Attack", "2", "2"))
        self.deck = deck

class PlayerDeck(Deck):
    def __init__(self):
        deck = []
    
        deck.append(Card("Free", "Viper", "Ship", "Attack", "1", "0"))
        deck.append(Card("Free", "Viper", "Ship", "Attack", "1", "0"))
            
        for i in range(8):
            deck.append(Card("Free", "Scout", "Ship", "Money", "1", "0"))

        self.deck = deck
        self.shuffle()

class DiscardPile(Deck):
    def __init__(self):
        deck = []
        self.deck = deck
        self.shuffle()

    def add_to_discard(self, card_to_add):
        self.deck.append(card_to_add)


class GameDeck(Deck):
    def __init__(self):
        deck = []

        card_factions = ["Star Empire", "Trade Federation", "Blob", "Machine Cult"]
        card_ships = ["Dreadnaught", "Corvette", "Battlecruiser", "Imperial Fighter", "Supply Mech"]
        card_bases = ["Blob Wheel", "Junkyard", "Recycling station", "Battle Station", "Brain World"]

        for faction in card_factions:
            for i in range(3):
                deck.append(Card(faction, random.choice(card_ships), "Ship", "Money", "1", "3"))
            
            for i in range(3):
                deck.append(Card(faction, random.choice(card_ships), "Ship", "Attack","4", "3"))

            for i in range(3):
                deck.append(Card(faction, random.choice(card_ships), "Ship", "Attack","2", "1"))

            deck.append(Card(faction, random.choice(card_ships), "Ship", "Attack","1", "2"))
            deck.append(Card(faction, random.choice(card_ships), "Ship", "Attack","1", "2"))
            deck.append(Card(faction, random.choice(card_ships), "Ship", "Attack","7", "7"))
            deck.append(Card(faction, random.choice(card_ships), "Ship", "Attack","5", "6"))            

            deck.append(Card(faction, random.choice(card_bases), "Base", "Attack","1", "3"))
            deck.append(Card(faction, random.choice(card_bases), "Base", "Attack","3", "5"))
            deck.append(Card(faction, random.choice(card_bases), "Base", "Attack","5", "8"))

        self.deck = deck
        self.shuffle()