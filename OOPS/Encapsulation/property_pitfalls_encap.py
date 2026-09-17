# 10. Create a class using @property and @setter for a private attribute.
# Then:
# 1. Show correct usage
# 2. Show how forgetting to use underscore prefix breaks encapsulation
# 3. Show what happens if you implement a setter without validation
# Focus: Python-specific encapsulation pitfalls, misuse of properties.

class Demo:
    def __init__(self):
        self.__value=0
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self,v):
        if v>=0:
            self.__value=v
        else:
            print("Invalid Value")
d=Demo()
d.value=10
print(d.value)
d.value-=5
print(d.value)