# To remove abiguity in variable types
from __future__ import annotations
from typing import List
import random

class Player:
    """
    A class representation of a player
    
    === Attributes ===
    score: int
    hand: List[int]
    
    """
    def __init__(self) -> None:
        """Initializes the class
        """
        self.score = 0
        self.hand = []
    
    def calc_score(self, card: int) -> None:
        """Calculates the player's current score

        Returns:
            int: the score
        """
        self.score += card
    
    def draw_card(self) -> None:
        """Draws a random card from the deck

        Returns:
            int: a randomly selected card
        """
        deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        card = random.choice(deck)
        self.hand.append(card)
        self.calc_score(card)
        if self.score > 21 and card == 11:
            self.eleven()
         
    
    def eleven(self) -> None:
        self.hand.remove(11)
        self.hand.append(1)
        self.score -= 10
        
class Dealer(Player):
    """
    A class representation of the dealer
    
    === Attributes ===
    score: int
    hand: List[int]
    """
    def __init__(self) -> None:
        super().__init__()
        while self.score < 17:
            card = self.draw_card()
            if card == 11 and self.score > 17:
                card = 1
                self.score -= 11
                self.score += 1
