# Names: Gerald Hill, Hoang Do
# Date: 9/30/24
# Desc: A program that plays a simple game of Yahtzee

from check_input import get_yes_no
from player import Player


def take_turn(player):
    ''' Takes a yahtzee turn for the player

    Args:
        - player (Player): player class representing the user

    Returns: none
    '''
    # Rolls dice and displays
    player.roll_dice()
    print(player)

    # Checks for win cons (three of a kinds is checked first)
    if player.has_three_of_a_kind():
        print("You got 3 of a kind!")
    elif player.has_pair():
        print("You got a pair!")
    elif player.has_series():
        print("You got a series of 3!")
    else:
        print("Aww. Too Bad.")
    
    # Displays points
    print("Score =", player.get_points())



def main():
    ''' Plays a simple game of Yahtzee '''
    # Initializes variables
    player = Player()
    choice = True

    print("-Yahtzee-",end="\n\n")
    
    # Loops until player chooses no
    while choice != False:
        take_turn(player)

        choice = get_yes_no("Play again? (Y/N): ")
        print()

    # Prints final score
    print("Game Over.")
    print("Final Score =", player.get_points())



main()