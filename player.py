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
        
class Dealer(Player):
    """
    A class representation of the dealer
    
    === Attributes ===
    score: int
    hand: List[int]
    """
    def __init__(self) -> None:
        super().__init__()
        deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,
                9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
        while self.score < 17:
            card = random.choice(deck)
            self.hand.append(card)
            deck.remove(card)
            self.score += card
            if self.score > 17 and card == 11:
                self.score += -10
                self.hand.remove(11)
                self.hand.append(1)
