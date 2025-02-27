# Names: Gerald Hill, Hoang Do
# Date: 10/21/24
# Desc: Plays a small RPG where you fight a dragon

from hero import Hero
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from flying_fire_dragon import FlyingFireDragon
from check_input import get_int_range
from random import randint

def main():
    '''Plays a small RPG where you fight a dragon'''
    # Asks user for name
    name = input("What is your name, challenger? ")
    print()

    hero = Hero(name, 50)
    dragons = [FireDragon(), FlyingDragon(), FlyingFireDragon()]
    game_over = False

    print(f"Welcome to dragon training, {hero.name}")
    print("You must defeat 3 dragons.")
    print()

    while game_over == False:
        print(hero)
        for i, dragon in enumerate(dragons):
            print(f"{i + 1}. {dragon}")
        # Asks user to pick a dragon to attack
        dragon_choice = get_int_range("Choose a dragon to attack: ", 1, len(dragons)) - 1
        print()

        print("Attack with:")
        print("1. Sword (2 D6)")
        print("2. Arrow (1 D12)")
        # Asks user to pick a weapon to attack with
        weapon_choice = get_int_range("Enter weapon: ", 1, 2)
        print()

        # User attacks
        if weapon_choice == 1:
            print(hero.basic_attack(dragons[dragon_choice]))
        else:
            print(hero.special_attack(dragons[dragon_choice]))

        # Checks for dead dragons
        for dragon in dragons:
            if dragon.hp == 0:
                dragons.remove(dragon)
        
        # Checks if game should end and moves loop to next iteration early
        if len(dragons) == 0:
            game_over = True
            print()
            print("Congratulations! You have defeated all three dragons, you have passed the trials.")
            continue

        # Selects a random dragon to attack and chooses which attack
        dragon_selected = randint(0, len(dragons) - 1)
        dragon_attack = randint(1, 2)

        # Dragon attacks
        if dragon_attack == 1:
            print(dragons[dragon_selected].basic_attack(hero))
        else:
            print(dragons[dragon_selected].special_attack(hero))
        print()

        # Checks if hero is dead
        if hero.hp == 0:
            game_over = True
            print()
            print("You Died!")

main()

        

