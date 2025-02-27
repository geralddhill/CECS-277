from dragon import Dragon
from fire import FireMixin
from random import randint
class FireDragon(Dragon, FireMixin):
    '''Fire Dragon class represents a fire dragon inherits from Dragon and FireMixin'''

    def __init__(self):
        '''Sets initial fire dragon stats'''
        super().__init__("Gronkle", 15, 3)

    def special_attack(self, opponent):
        '''Uses a random special move from FireMixin'''
        attack = randint(0,1)
        if attack == 0:
            return self.fireblast(opponent) 
        else:
            return self.fireball(opponent)
        