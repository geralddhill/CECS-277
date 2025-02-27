from door import Door
from random import randint
class ComboDoor(Door):
    """ComboDoor class represents a door with a combination lock.
            Attributes:
                _solution: Integer of the solution to unlock the door.
                _input: Integer of the most recent attempt to unlock the door.
    """

    def __init__(self) -> None:
        """Constructor for class ComboDoor

        Randomize the solution to a number 1-10.
        """
        self._solution: int = randint(1,10)
        self._input: int = 0


    def examine_door(self) -> str:
        """Returns a string description of the door.

        :return: Description of the door.
        """

        return f"You encounter a door with a combination lock. You can spin the dial to a number 1-10."


    def menu_options(self) -> str:
        """Returns a string with the menu options that user can choose from when attempting to unlock the door.

        :return: String of menu options for the door.
        """
        return f"Enter a number 1-10:"


    def get_menu_max(self) -> int:
        """Returns the number of options in the above menu for check input.

        :return: Maximum number of menu options for the door.
        """
        return 10


    def attempt(self, option: int) -> str:
        """ Runs the logic for the user's attempt to unlock the door.

        Passes in the user’s menu selection. Use this value to update the input attribute.
        Return a string describing the user’s attempt.

        :param option: Integer representing the menu option chosen by the user.
        :type option: int

        :return: String describing the attempt to unlock the door.

        :raise ValueError: Parameter option can only be in range 1-10.
        """
        if option < 1 or option > self.get_menu_max():
            raise ValueError(f"Parameter option can only be in range 1-{self.get_menu_max()}.")

        self._input = option
        return f"You turn the dial to... {self._input}"


    def is_unlocked(self) -> bool:
        """Returns the number of options in the above menu for check input.

        :return: Maximum number of menu options for the door.
        """
        return self._input == self._solution


    def clue(self) -> str:
        """Returns a hint for the user if their attempt was unsuccessful.

        :return: Hint for the user (str).
        """
        if self._input == self._solution:
            raise ValueError("Door is able to be unlocked. No need for clue.")

        if self._input < self._solution:
            return f"Try a higher value."
        else:
            return f"Try a lower value."


    def success(self) -> str:
        """Returns a congratulatory message if the user attempt was successful.

        :return: Congratulatory message for the user (str).
        """
        return f"You found the correct value and opened the door."
