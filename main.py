from Player import Player
import Deck

def main():
    player_one = Player(player_deck=Deck.PlayerDeck(), player_name="Player one")
    player_two = Player(player_deck=Deck.PlayerDeck(), player_name="Player two")
    
    player_one.get_hand()
    player_two.get_hand()

    card_deck = Deck.GameDeck()
    explorer_deck = Deck.ExplorerDeck()

    cards_on_the_table = []

    for i in range(5):
        cards_on_the_table.append(card_deck.draw())

    placement = 1
    print("Buy a card ------------------------------")
    for cards in cards_on_the_table:
        print(f"{placement}. {cards.get_card_info()}")
        placement = placement + 1

    if len(explorer_deck.deck) > 0:
        print(f"6. {len(explorer_deck.deck)} * {explorer_deck.deck[1].get_card_info()}")
    print("------------------------------------------")
    card_to_buy = int(input())

    if card_to_buy == 6:
        player_one.add_card_to_discard(explorer_deck.deck.pop())
    else:
        player_one.add_card_to_discard(cards_on_the_table[card_to_buy-1])

    for cards in player_one.player_card_hand:
        player_one.add_card_to_discard(cards)

    for cards in player_one.player_card_discard_pile:
        print(cards.get_card_info())
        
    player_one.print_player_data()

    player_one.print_points()
    player_two.print_points()

if __name__ == "__main__":
    main()