import random
import check_input

# Author: Gerald Hill, Hoang Khoi Do, Diego Ortega-Salazar
# Date: 8/26/24
# Description: Have computer generate a number, and then have the user repeatedly guess the number.
#              Tell user if guess is too low or too high. Keep track of guesses. Validate input.

def main():
    # Initiate correct value
    correctValue = random.randint(1, 100)
    userInput = 0

    print("-Guessing Game-")

    # First Guess
    userInput = check_input.get_int_range("I’m thinking of a number. Make a guess (1-100): ", 1, 100)
    numOfGuesses = 1

    # Checks guess and says if too low/high
    while True:
        if userInput < correctValue:
            print("Too low!",end=' ')
            userInput = check_input.get_int_range("Guess again (1-100): ", 1, 100)
        elif userInput > correctValue:
            print("Too high!",end=' ')
            userInput = check_input.get_int_range("Guess again (1-100): ", 1, 100)
        else:
            # If correct, break out of loop
            print("Correct! You got it in", numOfGuesses, " tries.")
            break
        # Increment counter
        numOfGuesses += 1

main()