import random
from Card import Card

class Setup:

    def __init__(self):
        #do nothing
        print("In Setup __init__")
        self.a_new_var = 0

    
    # Setup of player deck
    def setup_player_start_deck(self):
        #basic setup
        setup_player_deck = []
        
        # Viper
        setup_player_deck.append(Card("Free", "Viper", "Ship", "Attack", "1" "0"))
        setup_player_deck.append(Card("Free", "Viper", "Ship", "Attack", "1" "0"))
            
        # Loop for 8 Scouts
        for i in range(8):
            setup_player_deck.append(Card("Free", "Scout", "Ship", "Money", "1", "0"))

        return random.shuffle(setup_player_deck)

    # 10 explorer cards
    def deck_explorer(self):
        # 10 unaligned
        explorer_deck = []
        for i in range(10):
            explorer_deck.append(Card("Unaligned", "Explorer", "Ship", "Money", "2", "2"))
        
        return explorer_deck

    # Setup of standard deck
    def setup_card_deck(self):
        deck = []

        # Standard cards
        card_factions = ["Star Empire", "Trade Federation", "Blob", "Machine Cult"]
        card_ships = ["Dreadnaught", "Corvette", "Battlecruiser", "Imperial Fighter", "Supply Mech"]
        card_bases = ["Blob Wheel", "Junkyard", "Recycling station", "Battle Station", "Brain World"]

        # Loop di loop of cards for Deck
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

        random.shuffle(deck)
        return deck
        

        # Gula, 13 ship, 7 baser
        # blåa, 13 ship, 7 baser
        # grön, 15 ship,5 baser
        # röd, 14 ship,6 baser
        