from exceptions import InvalidInputError
from player import Player, Dealer
from blackjack import Blackjack

if __name__ == '__main__':
    game = Blackjack()
    play = input("Do you want to play a game of blackjack? Type 'y' for yes" +
                 " and 'n' for no: ")
    if play == 'y':
        game.play()
    elif play == 'n':
        exit()
    else:
        raise InvalidInputError