# Names: Gerald Hill, Hoang Do
# Date: 11/4/24
# Desc: Simulates a user having to open three kinds of doors. Uses factory pattern to implement.
from difficult_door_factory import DifficultDoorFactory
from door import Door
from check_input import get_int_range
from door_factory import DoorFactory
from easy_door_factory import EasyDoorFactory


def open_door(door: Door) -> None:
    """

    :param door: Door object that the user will try to unlock
    """
    # Prints door description
    print(door.examine_door())

    unlocked = False
    while not unlocked:
        # Prints door menu and accepts user input
        print(door.menu_options())
        user_input: int = get_int_range("Enter choice: ", 1, door.get_menu_max())
        # Attempts to unlock the door with the user input
        print(door.attempt(user_input))

        # Updates unlocked (to exit loop) and prints the correct message
        unlocked = door.is_unlocked()
        if unlocked:
            print(door.success())
        else:
            print(door.clue())



def main() -> None:
    """Simulates a user having to open three kinds of doors.

    Uses factory pattern to implement.
    """
    print("Welcome to the Escape Room.")
    print("You must unlock 3 doors to escape...")
    difficulty: int = get_int_range("Enter Difficulty (1. Easy 2. Hard): ", 1, 2)

    # Declares door_factory and assigns it to the correct factory based on the user's choice
    door_factory: DoorFactory
    if difficulty == 1:
        door_factory = EasyDoorFactory()
    else:
        door_factory = DifficultDoorFactory()

    # Gives the user 3 doors to try and open
    for i in range(3):
        door = door_factory.create_door()
        open_door(door)
        print()

    print("Congratulations! You escaped... this time.")


main()