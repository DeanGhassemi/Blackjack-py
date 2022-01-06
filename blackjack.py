# To remove abiguity in variable types
from __future__ import annotations
# Classes
from player import Player, Dealer
from exceptions import InvalidInputError

class Blackjack:
    """
    A class representation of Game
    
    === Attributes ===
    winer: bool
    client: Player
    dealer: dealer
    """
    def __init__(self) -> None:
        self.client = Player()
        self.dealer = Dealer()
        self.winner = False

    def play(self) -> None:
        self.client.draw_card()
        self.client.draw_card()
        self.winner = False
        while(not self.winner):
            print("Your hand: ", self.client.hand,  "Score: ", self.client.score)
            print("Dealer's first card: ", self.dealer.hand[0])
            card = input("\nWould you like to grab another card? 'y' or 'n': ")
            if card == 'y':
                self.client.draw_card()
            elif card == 'n':
                if self.dealer.score > 21:
                    print("\nYou win!")
                    self.prints()
                    self.winner = True
                elif self.client.score > self.dealer.score:
                    print("\nYou win!")
                    self.prints()
                    self.winner = True
                elif self.client.score < self.dealer.score:
                    print("\nYou lose!")
                    self.prints()
                    self.winner = True
                else:
                    print("\nDraw!")
                    self.prints()
                    self.winner = True
            else:
                raise InvalidInputError
            if self.client.score > 21:
                print("\nYou lose!")
                self.winner = True
                self.prints()
                break

    def prints(self) -> None:
        print("Dealer's hand: ", self.dealer.hand)
        print("Dealer's score: ", self.dealer.score)
        print("\nYour hand: ", self.client.hand)
        print("Your score: ", self.client.score)
