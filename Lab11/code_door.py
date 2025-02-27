from door import Door
from random import choice
class CodeDoor(Door):
    """CodeDoor class represents a three character code that must be entered correctly for the door to be unlocked.

    Each character in the code can be either 'X' or 'O' and the user can toggle between these for each key.

            Attributes:
                _solution: List of characters for the solution to unlock the door.
                _input: Current state of the keypad.
    """

    def __init__(self) -> None:
        """Constructor for class Door

        Randomizes the state of each character in the solution. Keypad starts in state "OOO".
        """
        self._solution: list[str] = ['O', 'O', 'O']
        # Makes sure input and solution won't be equal to start
        while self._solution == ['O', 'O', 'O']:
            for i in range(3):
                self._solution[i] = choice(['O', 'X'])

        self._input: list[str] = ['O', 'O', 'O']


    def examine_door(self) -> str:
        """Returns a string description of the door.

        :return: Description of the door.
        """

        return f"You encounter a coded door, you must enter the correct code to open the door. There are 3 characters displayed, each one can be toggled to either an 'X' or an 'O'. You can press the key under each character to toggle it."


    def menu_options(self) -> str:
        """Returns a string with the menu options that user can choose from when attempting to unlock the door.

        :return: String of menu options for the door.
        """
        return f"1. Press Key 1\n2. Press Key 2\n3. Press Key 3"


    def get_menu_max(self) -> int:
        """Returns the number of options in the above menu for check input.

        :return: Maximum number of menu options for the door.
        """
        return 3


    def attempt(self, option: int) -> str:
        """ Runs the logic for the user's attempt to unlock the door.

        Passes in the user’s menu selection. Use this value to update the input attribute.
        Return a string describing the user’s attempt.

        :param option: Integer representing the menu option chosen by the user.
        :type option: int

        :return: String describing the attempt to unlock the door.

        :raise ValueError: Parameter option can only be in range 1-2.
        """
        if option < 1 or option > self.get_menu_max():
            raise ValueError(f"Parameter option can only be in range 1-{self.get_menu_max()}.")

        if self._input[option - 1] == 'X':
            self._input[option - 1] = 'O'
        elif self._input[option - 1] == 'O':
            self._input[option - 1] = 'X'
        else:
            raise ValueError("Solution contains invalid characters.")

        if option == 1:
            return "You toggle the first character"
        if option == 2:
            return "You toggle the second character"
        else:
            return "You toggle the third character"




    def is_unlocked(self) -> bool:
        """Returns the number of options in the above menu for check input.

        :return: Maximum number of menu options for the door.
        """
        return self._input == self._solution


    def clue(self) -> str:
        """Returns a hint for the user if their attempt was unsuccessful.

        :return: Hint for the user (str).
        """
        num_correct: int = 0
        for i in range(self.get_menu_max()):
            if self._input[i] == self._solution[i]:
                num_correct += 1

        return f"{num_correct} keys are correct."


    def success(self) -> str:
        """Returns a congratulatory message if the user attempt was successful.

        :return: Congratulatory message for the user (str).
        """
        return f"You entered the correct code and opened the door."
