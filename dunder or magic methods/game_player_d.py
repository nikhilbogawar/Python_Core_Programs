# Create a class Player with:
# •	attributes: name, health, attack_power
# •	method: attack(enemy)
# Implement:
# •	__str__()
# •	__add__() → combine attack powers
# •	__sub__() → reduce health after attack
# •	__gt__() → compare health
# •	__eq__() → compare attack power
class Player:
    def __init__(self,name,health,attack_power):
        self.name=name
        self.health=health
        self.attack_power=attack_power
    def attack(self,enemy):
        enemy.health = enemy.health - self.attack_power
        if enemy.health<0:
            enemy.health=0
        print(f"{self.name} attacked {enemy.name}! {enemy.name}'s health is now {enemy.health}")
    def __str__(self):
        return f"Name : {self.name}\nHealth : {self.health}\nAttack Power : {self.attack_power}"
    def __add__(self, other):
        return self.attack_power+other.attack_power
    def __sub__(self, other):
        return self.health-other.attack_power
    def __gt__(self, other):
        return self.health>other.health
    def __eq__(self, other):
        return self.attack_power==other.attack_power
p1=Player("Nikhil",100,85)
p2=Player("Arjun",98,80)
print(p1)
print(p2)
print(p1+p2)
print(p1-p2)
print(p1>p2)
print(p1==p2)
p1.attack(p2)
p2.attack(p1)