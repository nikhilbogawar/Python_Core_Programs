# 12.
# Create:
# • Character → base class
# • Warrior, Archer, Mage subclasses
# Each subclass:
# • Overrides attack()
# • Encapsulates health with @property
# • Prevents negative HP
# • Uses class attributes for shared attributes (e.g., stamina_cost)
# Demonstrate polymorphic combat simulation.
class Character:
    def __init__(self, hp):
        self.__hp = hp
    @property
    def health(self):
        return self.__hp
    @health.setter
    def health(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value
class Warrior(Character):
    def attack(self):
        return "Warrior strikes"
class Archer(Character):
    def attack(self):
        return "Archer shoots"
class Mage(Character):
    def attack(self):
        return "Mage casts spell"
chars = [Warrior(100), Archer(80), Mage(60)]
for c in chars:
    print(c.attack(), "HP:", c.health)
