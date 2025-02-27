from cipher import *
class Caesar(Cipher):
    ''' Represent the Caesar cipher
    Inherits:
        Cipher() (from cipher.py)
    Attributes:
        _alphabet: str (from Cipher)
        _shift: int
    '''
    def __init__(self, shift) -> None:
        '''Initializes Caesar class with the attributes from the parent class and the shift interval'''
        # init the Casesar class with attribute shift and inherit the attribute alphabet from Cipher
        super().__init__()
        self._shift = shift

    def _encrypt_letter(self, letter):
        '''Encrypts a single passed in letter using the Caesar cipher'''
        # return the encrypted letter by using Caesar
        letter_location = self._alphabet.index(letter)
        encoded_letter_location = (letter_location + self._shift) % 26
        return self._alphabet[encoded_letter_location]
    

    def _decrypt_letter(self, letter):
        '''Decrypts a single passed in letter using the Caesar cipher'''
        # return the decrypted letter by using Caesar
        letter_location = self._alphabet.index(letter)
        decoded_letter_location = (letter_location - self._shift) % 26
        return self._alphabet[decoded_letter_location]
             
    
