# Names: Gerald Hill, Hoang Do
# Date: 10/28/24
# Desc: A dungeon game where a player moves across a map and fights monsters to get to the finish

from entity import Entity
from hero import Hero
from map1 import Map
from enemy import Enemy
from random import randint
import check_input

def main():
    """A dungeon game where a player moves across a map and fights monsters to get to the finish"""
    name = input("What is your name, traveler? ")
    h = Hero(name)
    m = Map()
    # Reveals initial hero position
    m.reveal(h.loc)
    
    choice = 0
    while choice != 5:
        e = Enemy()
        print(h)
        print(m.show_map(h.loc))
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")
        choice = check_input.get_int_range("Enter choice: ", 1,5)

        # Makes character move based on choice
        map_char = ''
        if choice == 1:
            map_char = h.go_north()

        elif choice == 2:
            map_char = h.go_south()

        elif choice == 3:
            map_char = h.go_east()

        elif choice == 4:
            map_char = h.go_west()

        # Takes action based on map character
        if map_char == 'o':
            print("You cannot go that way...")

        elif map_char == 'n':
            print("There is nothing here...")

        elif map_char == 'm':
            print(f"You encounter {e.name}")
            print(e)
            while e.hp != 0 or h.hp != 0:
                print(f"1. Attack {e.name}")
                print("2. Runaway")
                attack_choice = check_input.get_int_range("Enter Choice: ", 1, 2)
                # If the user attacks
                if attack_choice == 1:
                    print(h.attack(e))

                    if e.hp == 0:
                        print(f"You have slain a {e.name}")
                        m.remove_at_loc(h.loc)
                        break

                    # e can only attack h if it is not dead
                    print(e.attack(h))

                    if h.hp == 0:
                        print("You have been defeated")
                        break
                # If the user runs away, picks a random direction to run in
                else:
                    choice = randint(1, 4)
                    if choice == 1:
                        h.go_south()

                    elif choice == 2:
                        h.go_north()

                    elif choice == 3:
                        h.go_west()

                    elif choice == 4:
                        h.go_east()

                    break

        elif map_char == 'i':
            h.heal()
            print("You found a Health Potion! You drink it to restore your health.")
            m.remove_at_loc(h.loc)

        elif map_char == 's':
            print("You ended up at the start of the dungeon.")

        elif map_char == 'f':
            print("Congratulations! You found the exit.")
            print("game over")
            break

        else:
            print("this should never happen")
            
main()