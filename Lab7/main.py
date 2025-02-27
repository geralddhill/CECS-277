# Names: Gerald Hill, Hoang Do
# Date: 10/7/24
# Desc: Allows user to decode and encode encrypted messages

from check_input import get_int_range, get_int
from cipher import Cipher
from caesar import Caesar


def main():
    menu_choice = 0
    cipher_choice = 0

    while menu_choice != 3:
        '''Allows user to decode and encode encrypted messages'''
        # Displays menu and gets input from user
        print("Secret Decoder Ring:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        menu_choice = get_int_range("", 1, 3)
        # Early return if use wants to quit
        if menu_choice == 3:
            return
        print()

        # Displays cipher choice menu to user and gets input
        if menu_choice == 1:
            print("Enter encryption type:")
        elif menu_choice == 2:
            print("Enter decryption type:")
        print("1. Atbash")
        print("2. Caesar")
        cipher_choice = get_int_range("", 1, 2)

        # If encrypting, get message choice
        message = None
        if menu_choice == 1:
            message = input("Enter message: ")
            
        # Creates encryption based on cipher choice
        cipher = None
        if cipher_choice == 1:
            cipher = Cipher()
        elif cipher_choice == 2:
            shift = get_int("Enter shift value: ")
            cipher = Caesar(shift)

        # Performs correct action based on main menu choice
        if menu_choice == 1:
            message_encrypted = cipher.encrypt_message(message)
            file = open("message.txt", 'w')
            file.write(message_encrypted)
            file.close()
            print("Encrypted message saved to \"message.txt\".")
        
        if menu_choice == 2:
            print("Reading encrypted message from “message.txt”.")
            file = open("message.txt", 'r')
            message_encrypted = file.read()
            file.close
            message = cipher.decrypt_message(message_encrypted)
            print("Decrypted message:", message)



main()