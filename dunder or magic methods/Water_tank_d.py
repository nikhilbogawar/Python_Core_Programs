# Sir Method:---------------------------------------------------
class WaterTank:
    def __init__(self, tn: str, wl: int):
        self.tank_name = tn
        self.water_level = wl
    def __add__(self, o2: int):
        self.water_level += o2
        return self
    def __sub__(self, o2: int):
        self.water_level -= o2
        return self
    def __truediv__(self, o2: int):
        l = self.water_level / o2
        print(f"water level divided by {o2} tanks : ", end="")
        return l
    def __str__(self):
        return f"Tank Name : {self.tank_name}\nWater Level: {self.water_level}"
    def __repr__(self):
        return str(self.water_level)
tank1 = WaterTank(tn="tank1", wl=30)
print(tank1 + 20)
print(tank1 / 5)
print([tank1])

# My Method:--------------------------------------------------------
# class WaterTank:
#     number_of_tanks=0
#     def __init__(self,tank_name,water_level):
#         self.tank_name=tank_name
#         self.water_level=water_level
#         WaterTank.number_of_tanks+=1
#     def __add__(self, other):
#         return self.water_level+other.water_level
#     def __sub__(self, other):
#         return self.water_level-other.water_level
#     def __truediv__(self, other):
#         return self.water_level/other.number_of_tanks
#     def __str__(self):
#         return f"Tank Name : {self.tank_name} | Water Level : {self.water_level}"
#     def __repr__(self):
#         return f"Current Water Level : {self.water_level}"
# w1=WaterTank("Tank1",8)
# w2=WaterTank("Tank2",6)
# print(w1)
# print(w2)
# print("Fill Water:",w1+w2)
# print("Consume Water:",w1-w2)
# print("water equally among a given number of tanks:",(w1+w2)/WaterTank.number_of_tanks)
# print(repr(w1))