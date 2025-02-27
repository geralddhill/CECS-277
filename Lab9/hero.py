from entity import Entity
from random import randint

class Hero(Entity):
    '''
        Hero class inherits from entity
    '''    

    def basic_attack(self, opponent):
        '''represents the basic attack of the hero'''
        dmg = randint(1, 6) + randint(1, 6)
        opponent.take_damage(dmg)
        return f"{self.name} slashes the {opponent.name} with their sword for {dmg} damage"
    
    def special_attack(self, opponent):
        '''represents the special attack of the hero'''
        dmg = randint(1,12)
        opponent.take_damage(dmg)
        return f"{self.name} hits the {opponent.name} with an arrow for {dmg} damage!"
        
