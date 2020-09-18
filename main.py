from Player import Player
import Deck

def main():
    player_one = Player(player_deck=Deck.PlayerDeck())
    player_two = Player(player_deck=Deck.PlayerDeck())

    card_deck = Deck.GameDeck()
    explorer_deck = Deck.ExplorerDeck()

    for cards in card_deck:
        print(cards.card_faction +" - "+ cards.card_type +" - "+ cards.card_name)


if __name__ == "__main__":
    main()