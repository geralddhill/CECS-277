import random

class Die:
    '''
    Represents a single Die. Defaults to 6-sided die
    Attributes: 
    side(int): number of sides on the die
    value(int): the value of the rolled die.
    '''
    def __init__(self, side = 6):
        '''Initializes dice and rolls it for the first time'''
        self._side = side
        self._value = self.roll()

    def roll(self):
        '''Rolls the dice'''
        self._value = random.randint(1, 6)
        return self._value
    
    def __str__(self):
        '''Returns the dice's value as a string'''
        return str(self._value)
    
    def __lt__(self, other):
        '''Returns true if the current dice's value is less than the other's'''
        return self._value < other._value
    
    def __eq__(self, other):
        '''Returns true if the current dice's value is equal to the other's'''
        return self._value == other._value
    
    def __sub__(self, other):
        '''Subtracts the dices' values'''
        return self._value - other._value