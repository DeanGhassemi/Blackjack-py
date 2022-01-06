# To remove abiguity in variable types
from __future__ import annotations
# Classes
from player import Player, Dealer
from exceptions import InvalidInputError
from typing import List
import random

class Blackjack:
    """
    A class representation of Game
    
    === Attributes ===
    winer: bool
    client: Player
    dealer: dealer
    deck: List[int]
    """
    def __init__(self) -> None:
        self.client = Player()
        self.dealer = Dealer()
        self.winner = False
        self.deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,
                     9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,
                     11,11,11]
        
    def draw_card(self, p: Player) -> None:
        card = random.choice(self.deck)
        p.hand.append(card)
        self.deck.remove(card)
        p.score += card
        if p.score > 21 and card == 11:
            p.score += -10
            p.hand.remove(11)
            p.hand.append(1)
        
    def play(self) -> None:
        self.draw_card(self.client)
        self.draw_card(self.client)
        self.winner = False
        while(not self.winner):
            print("Your hand: ", self.client.hand,
                  "Score: ", self.client.score)
            print("Dealer's first card: ", self.dealer.hand[0])
            card = input("\nWould you like to grab another card? 'y' or 'n': ")
            if card == 'y':
                self.draw_card(self.client)
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
