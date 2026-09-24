# 10.
# Create:
# • Abstract class MenuItem with get_price()
# • Subclasses: Pizza, Burger, Drink
# • Order class containing a list of items (composition)
# • Encapsulate the list internally
# • Override methods to apply custom pricing logic for each food type
from abc import ABC, abstractmethod
class MenuItem(ABC):
    @abstractmethod
    def get_price(self):
        pass
class Pizza(MenuItem):
    def get_price(self):
        return 200
class Burger(MenuItem):
    def get_price(self):
        return 100
class Drink(MenuItem):
    def get_price(self):
        return 50
class Order:
    def __init__(self):
        self.__items = []
    def add_item(self, item):
        self.__items.append(item)
    def total(self):
        total_price = 0
        for item in self.__items:
            total_price = total_price + item.get_price()
        return total_price
order1 = Order()
order1.add_item(Pizza())
order1.add_item(Drink())
print("Total:", order1.total())