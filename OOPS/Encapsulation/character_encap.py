# 6. Create a Character class with:
# • private _health
# • methods to damage(points) and heal(points)
# • health cannot drop below 0 or exceed max limit
# • expose only current health through a read-only getter

class Character:
    def __init__(self,max_health=100):
        self.__health=max_health
        self.__max_health=max_health
    def damage(self,points):
        self.__health=max(0,self.__health-points)
    def heal(self,points):
        self.__health=min(self.__max_health,self.__health+points)
    def get_health(self):
        return self.__health
c=Character(100)
c.damage(45)
print(c.get_health())
c.heal(60)
print(c.get_health())
c.damage(200)
print(c.get_health())