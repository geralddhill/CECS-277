from door import Door
from random import randint
class BasicDoor(Door):
    """BasicDoor class represents a normal push/pull door
            Attributes:
                _solution: Integer of the solution to unlock the door.
                _input: Integer of the most recent attempt to unlock the door.
    """

    def __init__(self) -> None:
        """Constructor for class BasicDoor

        Randomizes the solution to either push (1) or pull (2).
        """
        self._solution: int = randint(1,2)
        self._input: int = 0


    def examine_door(self) -> str:
        """Returns a string description of the door.

        :return: Description of the door.
        """

        return f"You encounter a basic door. You can either push it or pull it to open."


    def menu_options(self) -> str:
        """Returns a string with the menu options that user can choose from when attempting to unlock the door.

        :return: String of menu options for the door.
        """
        return f"1. Push\n2. Pull"


    def get_menu_max(self) -> int:
        """Returns the number of options in the above menu for check input.

        :return: Maximum number of menu options for the door.
        """
        return 2


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

        self._input = option
        if self._input == 1:
            return f"You push the door."
        else:
            return f"You pull the door."


    def is_unlocked(self) -> bool:
        """Returns the number of options in the above menu for check input.

        :return: Maximum number of menu options for the door.
        """
        return self._input == self._solution


    def clue(self) -> str:
        """Returns a hint for the user if their attempt was unsuccessful.

        :return: Hint for the user (str).
        """
        return f"Try the other way."


    def success(self) -> str:
        """Returns a congratulatory message if the user attempt was successful.

        :return: Congratulatory message for the user (str).
        """
        return f"Congratulations, you opened the door."
        

