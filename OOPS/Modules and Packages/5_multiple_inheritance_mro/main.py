# 5. Create three modules:
# Module A: class Animal
# Module B: class Walkable
# Module C: class Dog that inherits from both Animal and Walkable
# Demonstrate method resolution order (MRO) by calling overridden methods and
# printing the MRO.
from dog import Dog
d=Dog()
d.sound()
d.move()
print(Dog.mro())