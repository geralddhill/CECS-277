class Cipher:
    ''' Represents the Atbash cypher and proviedes a framework for other cipher classes
    Attributes:
        _alphabet: str
    '''
    def __init__(self) -> None:
        '''Initializes cipher class with an _alphabet string'''
        self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt_message(self, message):
        '''Encrypts a message using the Atbash cypher; uses _encrypt_letter()'''
        encrypt_str = ""
        message_upper = message.upper()
        for char in message_upper:
            if 'A' <= char <= 'Z':
                char = self._encrypt_letter(char)
            encrypt_str += char
        return encrypt_str
    
    def decrypt_message(self, message):
        '''Decrypts a message using the Atbash cypher; uses _decrypt_letter()'''
        decrypt_str = ""
        message_upper = message.upper()
        for char in message_upper:
            if 'A' <= char <= 'Z':
                char = self._decrypt_letter(char)
            decrypt_str += char
        return decrypt_str

    def _encrypt_letter(self, letter):
        '''Encrypts a single passed in letter using the Atbash cipher'''
        original_letter_locaction = self._alphabet.index(letter)
        encoded_letter_location = 25 - original_letter_locaction
        return self._alphabet[encoded_letter_location]
    
    def _decrypt_letter(self, letter):
        '''Decrypts a single passed in letter using the Atbash cipher'''
        encoded_letter_location = self._alphabet.index(letter)
        decrypted_letter_location = 25 - encoded_letter_location
        return self._alphabet[decrypted_letter_location]
