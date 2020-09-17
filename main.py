from Setup import Setup
from Player import Player


def main():
    setup_the_deck = Setup()
    player_one = Player(setup_the_deck.setup_player_start_deck())
    player_two = Player(setup_the_deck.setup_player_start_deck())
    card_deck = setup_the_deck.setup_card_deck()
    card_deck_explorer = setup_the_deck.deck_explorer()


    for cards in card_deck:
        print(cards.card_faction +" - "+ cards.card_type +" - "+ cards.card_name)

if __name__ == "__main__":
    main()