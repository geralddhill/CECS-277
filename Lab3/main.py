# Name: Hoang Do, Gerald Hill
# Date: 9/9/24
# Desc: Plays a game of hangman with the user

import random
import check_input
from dictionary import words


def display_gallows(num_incorrect):
    ''' Prints gallows based on the number of incorrect guesses so far

    Args:
        - num_incorrect: number of incorrect guesses so far

    Returns: Nothing (prints to string)
    '''
    gallows = [
        '''
        ========
        ||/   |
        ||
        ||
        ||
        ||
        ''',
        '''
        ========
        ||/   |
        ||    o
        ||
        ||
        ||
        ''',
        '''
        ========
        ||/   |
        ||    o
        ||    |
        ||
        ||
        ''',
        '''
        ========
        ||/   |
        ||    o
        ||    |
        ||   /
        ||
        ''',
        '''
        ========
        ||/   |
        ||    o
        ||    |
        ||   / \\
        ||
        ''',
        '''
        ========
        ||/   |
        ||  \ o
        ||    |
        ||   / \\
        ||
        ''',
        '''
        ========
        ||/   |
        ||  \ o /
        ||    |
        ||   / \\
        ||
        '''
    ]
    print(gallows[num_incorrect])



def display_letters(letters):
    ''' Displays a list of letters with spaces in between

    Args:
        - letters: a list of letters

    Returns: nothing (prints to screen)
    '''
    for character in letters:
        print(character, end=' ')
    
    print()


    
def get_letters_remaining(incorrect, correct):
    ''' Returns all letters that haven't been guessed yet

    Args:
        - incorrect: all incorrect letters that have been guessed
        - correct: all correct letters that have been guessed

    Returns: Returns a list of letters that aren't in either given list
    '''
    list_of_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # Removes all incorrect letters
    for letter in incorrect:
        list_of_letters.remove(letter)
    # Removes all correct letters
    for letter in correct:
        list_of_letters.remove(letter)

    return list_of_letters



def main():
    ''' Plays a game of hangman with the user
    '''
    again = True

    while again == True:
        # Happens once every game
        correct_letter = []
        incorrect_letter = []
        guessed_word = ['_', '_', '_', '_', '_']
        random_word = random.choice(words)
        letters_correct = 0
        guesses_incorrect = 0
        print("-Hang man-\n")

        while guesses_incorrect < 6 and letters_correct < 5:
            # Beginning of every turn
            print("Incorrect selection: ", end = '')
            display_letters(incorrect_letter)
            display_gallows(guesses_incorrect)
            display_letters(guessed_word)
            print("Letters remaining: ", end='')
            display_letters(get_letters_remaining(incorrect_letter, correct_letter))
            
            # Guessing a letter
            letter = ""
            valid = False
            while valid == False:
                letter = input("\nEnter a letter: ").upper()
                # Validates input
                if not letter.isalpha():
                    print("That is not a letter")
                elif len(letter) != 1:
                    print("Enter one character")
                elif letter not in get_letters_remaining(incorrect_letter, correct_letter):
                    print("Please enter a letter that has not been entered before")
                else:
                    valid = True
                
            # Occurrs if letter is correct
            if letter in random_word:
                print("Correct!")
                correct_letter.append(letter)
                for i in range(len(random_word)):
                    if letter == random_word[i]:
                        guessed_word[i] = letter
                        letters_correct += 1
            # Occurs if letter is incorrect
            else:
                print("Incorrect")
                guesses_incorrect += 1
                incorrect_letter.append(letter)
        
        # Happens at the end of every game
        display_gallows(guesses_incorrect)
        display_letters(guessed_word)
        print()

        if guesses_incorrect == 6:
            print("You lose!")
        elif letters_correct == 5:
            print("You win!")
        # This should never occur
        else:
            print("Error")

        # Asks to play again
        again = check_input.get_yes_no("Play again (Y/N)? ")
        
main()