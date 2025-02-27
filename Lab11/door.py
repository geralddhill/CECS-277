from abc import ABC, abstractmethod

class Door(ABC):
    """Interface for all doors."""

    @abstractmethod
    def examine_door(self) -> str:
        """Returns a string description of the door.

        :return: Description of the door.
        """
        pass

    @abstractmethod
    def menu_options(self) -> str:
        """Returns a string with the menu options that user can choose from when attempting to unlock the door.

        :return : String of menu options for the door.
        """
        pass

    @abstractmethod
    def get_menu_max(self) -> int:
        """Returns the number of options in the above menu for check input.

        :return: Maximum number of menu options for the door.
        """
        pass

    @abstractmethod
    def attempt(self, option: int) -> str:
        """ Runs the logic for the user's attempt to unlock the door.

        Passes in the user’s menu selection. Use this value to update the input attribute.
        Return a string describing the user’s attempt.

        :param option: Integer representing the menu option chosen by the user.
        :type option: int
        
        :return: String describing the attempt to unlock the door.
        """
        pass

    @abstractmethod
    def is_unlocked(self) -> bool:
        """Checks to see if the door was unlocked by comparing the input attribute with the solution.

        :return: Returns true if it is unlocked, false otherwise.
        """
        pass

    @abstractmethod
    def clue(self) -> str:
        """Returns a hint for the user if their attempt was unsuccessful.

        :return: Hint for the user (str).
        """
        pass

    @abstractmethod
    def success(self) -> str:
        """Returns a congratulatory message if the user attempt was successful.

        :return: Congratulatory message for the user (str).
        """
        pass