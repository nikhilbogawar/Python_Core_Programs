# 7. Create:
# • An Engine class with private state like temperature
# • A Car class that uses an Engine but should:
# o Not allow users to manipulate engine temperature
# o Only expose methods like start_car() or cool_engine()
# Demonstrate why giving direct engine access is dangerous.
from multiprocessing.util import get_temp_dir


# class Engine:
#     def __init__(self):
#         self.__temperature=30
#     def cool(self):
#         self.__temperature-=10
#         # print(self.__temperature)
# class Car:
#     def __init__(self):
#         self.__engine=Engine()
#     def start_car(self):
#         print("Car Started")
#     def cool_engine(self):
#         self.__engine.cool()
# c=Car()
# c.start_car()
# c.cool_engine()

# sir method:-->>>
class Engine:
    def __init__(self,type):
        self.type=type
        self.__temp=32
    def cool_engine(self):
        self.__temp-=10
    def start_engine(self):
        self.__temp+=10
        print("Started Engine")
    def get_temp(self):
        print(self.__temp)
class Car:
    def __init__(self,brand,engine):
        self.brand=brand
        self.engine=engine
    def start_engine(self):
        self.engine.start_engine()
    def stop_car(self):
        self.engine.cool_engine()
c1=Car("BMW",Engine("V12"))
c1.start_engine()
c1.stop_car()
c2=Engine("V12")
c2.get_temp()