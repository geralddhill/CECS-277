from entity import Entity
from random import randint
from abc import abstractmethod

class Dragon(Entity):
    '''A dragon class that represents an abstract dragon'''

    def __init__(self, name, max_hp, num_sp):
        '''Runs entity init and adds the max number of special attacks'''
        super().__init__(name, max_hp)
        self._special_attacks = num_sp
    
    @property
    def special_attacks(self):
        '''Getter for the number of special attacks left'''
        return self._special_attacks
    
    def decrement_special_attacks(self):
        '''Decrements the number of special attacks by one'''
        self._special_attacks -= 1
        if self._special_attacks < 0:
            self._special_attacks = 0

    def basic_attack(self, opponent):
        '''Performs a basic attack and damages opponent'''
        dmg = randint(3,7)
        opponent.take_damage(dmg)
        return f"{self.name} smashes you with its tail for {dmg} damage"
        
    @abstractmethod
    def special_attack(self, opponent):
        pass

    def __str__(self) -> str:
        '''Retuns dragon as a string, same as entity, and adds the number of special attacks remaining'''
        entity_str = super().__str__()
        return f"{entity_str} \nSpecial attacks remaining: {self._special_attacks}"
