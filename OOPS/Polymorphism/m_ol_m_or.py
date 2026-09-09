# Explain the difference between method overriding and method overloading.
# Python does not natively support overloading — show how to simulate it using *args or default parameters.

# Method Overriding: A child class redefines a method from its parent.
# Method Overloading: Same method name with different parameter lists.
# Python doesn’t support this directly, but you can simulate it.

# Overriding Example
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

print(Dog().sound())  # Bark

# Simulated Overloading Example
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(2, 3))        # 5
print(calc.add(1, 2, 3, 4))  # 10
