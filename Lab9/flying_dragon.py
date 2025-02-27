from dragon import Dragon
from flying import FlyingMixin
from random import randint

class FlyingDragon(Dragon, FlyingMixin):
    '''Flying Dragon class represents a flying dragon inherits from Dragon and FlyingMixin'''

    def __init__(self):
        '''Sets initial flying dragon stats'''
        super().__init__("Timberjack", 10, 3)

    def special_attack(self, opponent):
        '''Uses a random special move from FlyingMixin'''
        move_choice = randint(0, 1)
        if move_choice == 0:
            return self.swoop(opponent)
        else:
            return self.windblast(opponent)