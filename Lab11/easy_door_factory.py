from basic_door import BasicDoor
from combo_door import ComboDoor
from door import Door
from random import randint
from door_factory import DoorFactory
from locked_door import LockedDoor


class EasyDoorFactory(DoorFactory):
    """Door factory that creates an instance or a random easy door.
    """

    def create_door(self) -> Door:
        """Factory method to create an instance of a door.

        Chooses randomly between BasicDoor, LockedDoor, and ComboDoor.

        :return: Door instance
        """
        door_choice: int = randint(1, 3)

        if door_choice == 1:
            return BasicDoor()
        elif door_choice == 2:
            return LockedDoor()
        else:
            return ComboDoor()
