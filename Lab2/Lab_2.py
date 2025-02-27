# Name: Gerald Hill, Hoang Do
# Date: 9/4/24
# Desc: Runs a set of games of Rock Paper Scissors between a player and a computer.

import random
import check_input

def weapon_menu():
    """ Displays menu for user weapon choice and returns the user's input

    Args: None

    Retruns: Returns a character corresponding to the user's choice (R, P, S, or B)
    """
    # Variable that will be true when input is valid
    valid = False

    # Iterates until valid input is given
    while valid == False:
        # Prints menu and asks for user input
        print("Choose your weapon: ")
        print("R. Rock")
        print("P. Paper")
        print("S. Scissors")
        print("B. Back")
        choice = input("")
        # Makes user input uppercase
        choice = choice.upper()
        # Validates input
        if choice == 'R' or choice == 'P' or choice == 'S' or choice == 'B':
            valid = True
        else:
            # Message for invalid input
            print("Please enter a valid input")

    # Returns a valid choice
    return choice



def comp_weapon():
    """ Randomly picks and returns a weapon choice for the computer

    Args: None

    Returns: Returns a character corresponding to the computer's choice (R, P, or S)
    """
    # Randomly generated number from 0-2
    computer = random.randint(0, 2)    
    
    # Assigns a char value for the corresponding int value
    if computer == 0:
        computer = "R"
    elif computer == 1:
        computer = "P"
    else:
        computer = "S"

    # Returns char value for weapon
    return computer



def find_winner(player, comp):
    """ Takes in weapon for both the player and computer and returns the winner of RPS.

    Args:
        player (char): The user's weapon input
        comp (char): The computer's weapon input

    Returns:
        A int that corresponds to the winner (0 = Tie, 1 = Player, 2 = Computer)
    """

    # Checks through all possible non-tie outcomes and returns the correct value
    if player == 'R' and comp == 'P':
        print("Computer wins")
        return 2
    elif player == 'R' and comp == 'S':
        print("You win")
        return 1
    elif player == 'P' and comp == 'R':
        print("You win")
        return 1
    elif player == 'P' and comp == 'S':
        print("Computer wins")
        return 2
    elif player == 'S' and comp == 'P':
        print("You win")
        return 1
    elif player == 'S' and comp == 'R':
        print("Computer wins")
        return 2
    
    # All other possible outcomes are ties; returns accordingly
    else:
        print("Tie")
        return 0 


def display_scores(player, comp):
    """ Displays the RPS scores for both the player and the computer

    Args:
        player (int): The user's score
        comp (int): The computer's score

    Returns:
        This function returns no value. It outputs to the screen
    """

    print("Player = ", player)
    print("Computer = ", comp)



def main():
    """ Runs a set of games of Rock Paper Scissors between a player and a computer. Contains main menu. """

    # Define loop exit variable and score variables
    finished = False
    player_score = 0
    comp_score = 0
    
    while finished == False:
        # Prints menu
        print("1. Play game")
        print("2. Show Score")
        print("3. Quit")
        #Gets user input
        option = check_input.get_int_range("", 1, 3)

        # Plays RPS games
        if option == 1:
            # Defines player choice so it is reset every set of games
            player_choice = ''
            while player_choice != 'B':
                # Gets player choice
                # If choice is B, gets out of loop
                player_choice = weapon_menu()
                if player_choice == 'B':
                    continue

                # Displays player choice
                elif player_choice == 'R':
                    print("You chose Rock")
                elif player_choice == 'P':
                    print("You chose Paper")
                elif player_choice == 'S':
                    print("You chose Scissors")

                # Gets computer choice
                comp_choice = comp_weapon()

                # Displays computer choice
                if comp_choice == 'R':
                    print("Computer chose Rock")
                elif comp_choice == 'P':
                    print("Computer chose Paper")
                elif comp_choice == 'S':
                    print("Computer chose Scissors")

                winner = find_winner(player_choice, comp_choice)

                if winner == 1:
                    player_score += 1
                elif winner == 2:
                    comp_score += 1
        
        # Displays Scores
        elif option == 2:
            display_scores(player_score, comp_score)

        # Exist and displays final score
        elif option == 3:
            print("Final Score:")
            display_scores(player_score, comp_score)
            finished = True

main()