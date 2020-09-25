from Player import Player
import Deck

def main():
    #--------------------------------------
    # Hand out cards and set up deck
    #--------------------------------------
    player_one = Player(player_deck=Deck.PlayerDeck(), player_name="Player one")
    player_two = Player(player_deck=Deck.PlayerDeck(), player_name="Player two")
    player_one.get_hand()
    player_two.get_hand()
    card_deck = Deck.GameDeck()
    explorer_deck = Deck.ExplorerDeck()
    cards_on_the_table = []
    for i in range(5):
        cards_on_the_table.append(card_deck.draw())
    
    game_on = True

    while game_on:
        
        #--------------------------------------
        # Attack
        #--------------------------------------
        player_money = 0
        player_attack = 0
        player_one.print_player_hand()

        for cards in player_one.player_card_hand:
            if cards.card_abillity == "Attack":
                player_attack = player_attack + int(cards.card_pimary_abillity_value)
                player_two.player_points = int(player_two.player_points) - int(cards.card_pimary_abillity_value)
            else:
                player_money = player_money + int(cards.card_pimary_abillity_value)

        print(f"Attacked with {player_attack}")
        player_one.print_points()
        player_two.print_points()
        
        if player_one.player_points <= 0 or player_two.player_points <= 0:
            if player_one.player_points > 0:
                print("Player one is the winner")
            else:
                print("Player two is the winner")
            break

        #--------------------------------------
        # Buy
        #--------------------------------------
        print("------------------------------")

        placement = 1
        cards_possible_to_buy = []
        for cards in cards_on_the_table:
            print(f"{placement}. {cards.get_card_info()}")
            if int(cards.card_cost) <= player_money:
                cards_possible_to_buy.append(placement)
                
            placement = placement + 1

        if len(explorer_deck.deck) > 0:
            print(f"6. {len(explorer_deck.deck)} * {explorer_deck.deck[1].get_card_info()}")
            if player_money >= 2:
                cards_possible_to_buy.append(6)

        print("7. Buy nothing")
        print("------------------------------------------")
        print(f"You have {player_money} credits to buy cards with")
        for possible in cards_possible_to_buy:
            print(possible, end=", ")

        card_to_buy = int(input())

        if card_to_buy == 6:
            player_one.add_card_to_discard(explorer_deck.deck.pop())
        
        if card_to_buy < 6:
            player_one.add_card_to_discard(cards_on_the_table[card_to_buy-1])
            cards_on_the_table[card_to_buy-1] = card_deck.draw()

        if card_to_buy == 7:
            game_on = False

        # add to discard pile and 
        # draw new card
        
        while len(player_one.player_card_hand) > 0:
            player_one.add_card_to_discard(player_one.player_card_hand.pop())
        #for cards in player_one.player_card_hand:

        player_one.get_hand()
    

if __name__ == "__main__":
    main()