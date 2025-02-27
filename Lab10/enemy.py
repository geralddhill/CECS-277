from entity import Entity
import random
class Enemy(Entity):
    """
        Enemy class represents an enemy entity
        Extends from Entity

        Attributes:
            _name: string
            _max_hp: int
            _hp: int
    """

    def __init__(self):
        super().__init__(name = random.choice(['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie', 'Werewolf', 'Wraith', 'Troll', 'Orc', 'Demon']), max_hp=random.randint(4,8))


    def attack(self, entity):
        """Attacks entity for 1-4 damage and returns a string describing the event"""
        damage = random.randint(1,4)
        entity.take_damage(damage)
        
        return f"{self._name} attacks {entity.name} for {damage} damage."
    