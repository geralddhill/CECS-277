from random import randint
class FireMixin:
    '''Mixin class Fire represents the special attacks'''

    def fireblast(self, opponent):
        '''fireblast method'''
        if self.special_attacks <= 0:
            return f"{self.name} tries to engulf {opponent.name} in flames, but it is all out of fuel."
        
        self.decrement_special_attacks()
        dmg = randint(5,9)
        opponent.take_damage(dmg)
        return f"{self.name} engulfs {opponent.name} in flames for {dmg} damage!"
    
    def fireball(self, opponent):
        '''fireball method'''
        if self.special_attacks <= 0:
            return f"{self.name} tries to spit a fireball at {opponent.name}, but it is all out of fuel."
        
        self.decrement_special_attacks()
        dmg = randint(4,8)
        opponent.take_damage(dmg)
        return f"{self.name} spits a fireball at {opponent.name} for {dmg} damage!"