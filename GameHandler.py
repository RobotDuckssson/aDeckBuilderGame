from Player import Player
import Deck

class GameHandler(object):

    def __init__(self):
        self.setup_game()
        self.game_on = True

        while self.game_on:
            self.player_attack()
            self.show_trade_deck()
            self.buy_card()
            self.discard_cards()
            self.get_new_hand()

    # Game setup
    def setup_game(self):
        self.player_one = Player(player_deck=Deck.PlayerDeck(), player_name="Player one")
        self.player_two = Player(player_deck=Deck.PlayerDeck(), player_name="Player two")
        self.player_one.get_hand()
        self.player_two.get_hand()
        self.card_deck = Deck.GameDeck()
        self.explorer_deck = Deck.ExplorerDeck()
        self.cards_on_the_table = []
        for i in range(5):
            self.cards_on_the_table.append(self.card_deck.draw())

    #Player attack
    def player_attack(self):
        
        player_attack = 0
        self.player_one.print_player_hand()

        for cards in self.player_one.player_card_hand:
            if cards.card_abillity == "Attack":
                player_attack = player_attack + int(cards.card_pimary_abillity_value)
                self.player_two.player_points = int(self.player_two.player_points) - int(cards.card_pimary_abillity_value)
            else:
                self.player_one.player_current_money = self.player_one.player_current_money + int(cards.card_pimary_abillity_value)

        print(f"Attacked with {player_attack}")
        self.player_one.print_points()
        self.player_two.print_points()

    # Shows the trade deck
    def show_trade_deck(self):
        if self.player_one.player_points <= 0 or self.player_two.player_points <= 0:
            if self.player_one.player_points > 0:
                print("Player one is the winner")
            else:
                print("Player two is the winner")
            
            self.game_on = False

        #--------------------------------------
        # Buy
        #--------------------------------------
        print("------------------------------")

        placement = 1
        cards_possible_to_buy = []
        for cards in self.cards_on_the_table:
            print(f"{placement}. {cards.get_card_info()}")
            if int(cards.card_cost) <= self.player_one.player_current_money:
                cards_possible_to_buy.append(placement)
                
            placement = placement + 1

        if len(self.explorer_deck.deck) > 0:
            print(f"6. {len(self.explorer_deck.deck)} * {self.explorer_deck.deck[1].get_card_info()}")
            if self.player_one.player_current_money >= 2:
                cards_possible_to_buy.append(6)

        print("7. Buy nothing")
        print("------------------------------------------")
        print(f"You have {self.player_one.player_current_money} credits to buy cards with")
        for possible in cards_possible_to_buy:
            print(possible, end=", ")

    # Handles the purchase, discards and gets new hand
    def buy_card(self):
        card_to_buy = int(input())
        if card_to_buy == 6:
            self.player_one.add_card_to_discard(self.explorer_deck.deck.pop())
        
        if card_to_buy < 6:
            self.player_one.add_card_to_discard(self.cards_on_the_table[card_to_buy-1])
            self.cards_on_the_table[card_to_buy-1] = self.card_deck.draw()

        if card_to_buy == 7:
            self.game_on = False

    def discard_cards(self):
                # add to discard pile and 
        # draw new card
        while len(self.player_one.player_card_hand) > 0:
            self.player_one.add_card_to_discard(self.player_one.player_card_hand.pop())
        #for cards in player_one.player_card_hand:

    def get_new_hand(self):
        self.player_one.get_hand()
