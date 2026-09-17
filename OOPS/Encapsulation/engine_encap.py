# 7. Create:
# • An Engine class with private state like temperature
# • A Car class that uses an Engine but should:
# o Not allow users to manipulate engine temperature
# o Only expose methods like start_car() or cool_engine()
# Demonstrate why giving direct engine access is dangerous.

class Engine:
    def __init__(self):
        self.__temperature=30
    def cool(self):
        self.__temperature-=10
        # print(self.__temperature)
class Car:
    def __init__(self):
        self.__engine=Engine()
    def start_car(self):
        print("Car Started")
    def cool_engine(self):
        self.__engine.cool()
c=Car()
c.start_car()
c.cool_engine()