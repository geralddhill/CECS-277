from door import Door
from random import choice
class DeadboltDoor(Door):
    """DeadboltDoor class represents a door with two deadbolts that must both be unlocked to unlock the door.

    Both deadbolts are randomized whether they are locked or unlocked to start, and the user must unlock both of them
    in order to unlock the door.

            Attributes:
                _bolt1: State of bolt 1 (bool); True is unlocked
                _bolt2: State of bolt 2 (bool); True is unlocked
    """

    def __init__(self) -> None:
        """Constructor for class LockedDoor

        Randomizes the state of each bolt.
        """
        self._bolt1: bool = True
        self._bolt2: bool = True

        # Makes sure both bolts aren't unlocked to start
        while self._bolt1 and self._bolt2:
            self._bolt1: bool = choice([True, False])
            self._bolt2: bool = choice([True, False])


    def examine_door(self) -> str:
        """Returns a string description of the door.

        :return: Description of the door.
        """

        return f"You encounter a double deadbolt door. Both deadbolts must be unlocked to open it, but you can't tell from looking at them whether they're locked or unlocked."


    def menu_options(self) -> str:
        """Returns a string with the menu options that user can choose from when attempting to unlock the door.

        :return: String of menu options for the door.
        """
        return f"1. Toggle Bolt 1\n2. Toggle Bolt 2"


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

        if option == 1:
            self._bolt1 = not self._bolt1
            return "You toggle the first bolt."
        else:
            self._bolt2 = not self._bolt2
            return "You toggle the second bolt."



    def is_unlocked(self) -> bool:
        """Returns the number of options in the above menu for check input.

        :return: Maximum number of menu options for the door.
        """
        return self._bolt1 and self._bolt2


    def clue(self) -> str:
        """Returns a hint for the user if their attempt was unsuccessful.

        :return: Hint for the user (str).
        """
        if self._bolt1 and self._bolt2:
            raise ValueError("Door is able to be unlocked. No need for clue.")

        if not self._bolt1 and not self._bolt2:
            return "You jiggle the door... it's completely locked."
        else:
            return "You jiggle the door... it seems like one of the bolts is unlocked."


    def success(self) -> str:
        """Returns a congratulatory message if the user attempt was successful.

        :return: Congratulatory message for the user (str).
        """
        return f"You unlocked both deadbolts and opened the door."
