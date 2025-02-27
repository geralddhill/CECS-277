from random import randint

class FlyingMixin:
    '''Mixin that can give a class access to flying special attacks'''

    def swoop(self, opponent):
        '''Performs the swoop special attack'''
        # Allows for early return if no energy
        if self.special_attacks <= 0:
            return f"{self.name} tries to swoop at {opponent.name}, but it is all out of energy."
        
        dmg = randint(4, 8)
        opponent.take_damage(dmg)
        self.decrement_special_attacks()
        return f"{self.name} swoops at {opponent.name} for {dmg} damage!"
    
    def windblast(self, opponent):
        '''Performs the windblast special attack'''
        # Allows for early return if no energy
        if self.special_attacks <= 0:
            return f"{self.name} tries to blow a gust of wind at {opponent.name}, but it is all out of energy."
        
        dmg = randint(3, 7)
        opponent.take_damage(dmg)
        self.decrement_special_attacks()
        return f"{self.name} blows a strong gust of wind at {opponent.name} for {dmg} damage!"