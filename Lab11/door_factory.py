from abc import ABC, abstractmethod
from door import Door

class DoorFactory(ABC):
    """Interface for door factories."""

    @abstractmethod
    def create_door(self):
        """Factory method to create an instance of a door.

        Door type is chosen at random.

        :return: Door instance
        """
        pass