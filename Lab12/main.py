# Names: Gerald Hill, Hoang Do
# Date: 11/13/24
# Desc: A game that has the user add food to their plate without going over the weight or area limit of a paper plate.

from check_input import get_int_range
from green_beans import GreenBeans
from large_plate import LargePlate
from pie import Pie
from plate import Plate
from potatoes import Potatoes
from small_plate import SmallPlate
from stuffing import Stuffing
from turkey import Turkey


def examine_plate(p: Plate) -> bool:
    """ Displays plate information and hints to the user.

    :param p: :class:`Plate` to examine
    :return: True if the plate is full and spills. False if the plate is not full.
    """
    print(p.description())

    # Early return if plate overflows
    if p.area() <= 0:
        print("Your plate isn't big enough for this much food! Your food spills over the edge.")
        return True
    elif p.weight() <= 0:
        print("Your plate isn't sturdy enough for this much food! Your food spills over the edge.")
        return True

    # Weight hints
    print("Sturdiness: ",end='')
    if p.weight() >= 13:
        print("Strong")
    elif p.weight() >= 7:
        print("Weak")
    elif p.weight() >= 1:
        print("Bending")
    else:
        # This should never occur
        raise ValueError("Impossible weight of plate.")

    # Area hints
    print("Space available: ",end='')
    if p.area() >= 41:
        print("Plenty")
    elif p.area() >= 21:
        print("Some")
    elif p.area() >= 1:
        print("A tiny bit")
    else:
        # This should never occur
        raise ValueError("Impossible area of plate.")

    return False



def main():
    """A game that has the user add food to their plate without going over the weight or area limit of a paper plate."""
    plate: Plate
    game_over: bool = False

    # Prints starting menu and lets user choose a plate
    print("- Thanksgiving Dinner -")
    print("Serve yourself as much food as you like from the buffet, but make sure that your plate will hold without spilling everywhere!")
    print("Choose a plate:")
    print("1. Small Sturdy Plate")
    print("2. Large Flimsy Plate")
    plate_choice = get_int_range("", 1, 2)

    # Creates plate based on user choice
    if plate_choice == 1:
        plate = SmallPlate()
    else:
        plate = LargePlate()

    while not game_over:
        # Prints food menu and lets the user choose which food to add to the plate
        print("1. Turkey")
        print("2. Stuffing")
        print("3. Potatoes")
        print("4. Green Beans")
        print("5. Pie")
        print("6. Quit")
        food_choice = get_int_range("", 1, 6)

        # Decorates plate with food choice
        if food_choice == 1:
            plate = Turkey(plate)
        elif food_choice == 2:
            plate = Stuffing(plate)
        elif food_choice == 3:
            plate = Potatoes(plate)
        elif food_choice == 4:
            plate = GreenBeans(plate)
        elif food_choice == 5:
            plate = Pie(plate)
        else:
            print(plate.description())
            print(f"Good job! You made it to the table with {plate.count()} items.")
            print(f"There was still {plate.area()} square inches left on your plate.")
            print(f"Your plate could have held {plate.weight()} more ounces of food.")
            print("Don't worry, you can always go back for more. Happy Thanksgiving!")
            game_over = True
            break

        game_over = examine_plate(plate)





main()