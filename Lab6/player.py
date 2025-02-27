from die import Die

class Player:
    def __init__(self):
        '''Initializes player class with a list of three dice and zero points'''
        self._dice = sorted([Die(), Die(), Die()])
        self._points = 0

    def get_points(self):
        '''Returns the number of points the player has'''
        return self._points
    
    def roll_dice(self):
        '''Rolls all three dice'''
        for d in self._dice:
            d.roll()
        self._dice.sort()

    def has_pair(self):
        '''Returns true if there exists a pair within the three dice'''
        # Checks for all possible pairs
        if self._dice[0] == self._dice[1]:
            self._points += 1
            return True
        elif self._dice[0] == self._dice[2]:
            self._points += 1
            return True
        elif self._dice[1] == self._dice[2]:
            self._points += 1
            return True
        return False
    
    def has_three_of_a_kind(self):
        '''Returns true if there exists three of the same number within the three dice'''
        if self._dice[0] == self._dice[1] and self.dice[0] == self.dice[2]:
            self._points += 3
            return True
        return False
    
    def has_series(self):
        '''Returns true if there exists a three number series within the three dice'''
        # Makes sure the difference between each adjacent variable is 1 (since list is sorted)
        if self._dice[1] - self._dice[0] == 1 and self._dice[2] - self._dice[1] == 1:
            self._points += 2
            return True
        return False
        
    def __str__(self):
        '''Returns the player's dice as a string'''
        s = ""
        # Adds each dice to string
        for i, d in enumerate(self._dice):
            s += "D" + str(i + 1) + "=" + str(d) + ", "
        return s