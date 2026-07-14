# Build an Inventory class that:
# •	Tracks the total number of items across all inventories.
# •	Each instance maintains its own stock dictionary ({"item": quantity}).
# •	Provides a method to add or remove stock.
# •	Allows updating a minimum stock threshold globally.
# •	Offers a static checker to verify if a stock level is below threshold.
# Demonstrate:
# 1.	Managing multiple inventories.
# 2.	Adjusting stock threshold.
# 3.	Using static validation inside the instance logic.

class Inventory:
    total_items = 0
    min_stock = 5

    def __init__(self):
        self.stock = {}

    def add_stock(self, item, qty):
        self.stock[item] = self.stock.get(item, 0) + qty
        Inventory.total_items += qty

    def remove_stock(self, item, qty):
        if item in self.stock and self.stock[item] >= qty:
            self.stock[item] -= qty
            Inventory.total_items -= qty

    @classmethod
    def update_threshold(cls, new_min):
        cls.min_stock = new_min

    @staticmethod
    def is_below_threshold(qty):
        return qty < Inventory.min_stock

# Demo
inv1 = Inventory()
inv1.add_stock("Apples", 10)
print(inv1.stock)
print(Inventory.is_below_threshold(3))

