import abc
class Entity(abc.ABC):
    '''
        Entity class represents an entity such as hero or enemy
        
        Attributes:
            _name: string
            _max_hp: int
            _hp: int
    '''

    def __init__(self, name, max_hp):
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp


    @property
    def name(self):
        '''Getter for name'''
        return self._name


    @property
    def hp(self):
        return self._hp


    def take_damage(self, dmg):
        '''take_damage method that subtracts the dmg from the hp'''
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0


    def heal(self):
        '''heal method to restore the entity hp'''
        self._hp = self._max_hp
    def __str__(self) -> str:
        '''return the name and the hp/maxhp'''
        return f"{self._name} \nHP: {self._hp}/{self._max_hp}"

    
    @abc.abstractmethod
    def attack(self, entity):
        '''anstract method'''
        pass
    