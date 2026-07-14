# Design a class Product that:
# •	Maintains a base tax rate applicable to all products.
# •	Each product has a name and base price.
# •	Has a method to compute final price including tax.
# •	Can change tax rate for all products using one method.
# •	Includes a function to check whether a given price is valid or not (non-negative and realistic).
# Demonstrate:
# 1.	Creating multiple products.
# 2.	Changing the tax rate.
# 3.	Showing updated prices and validity checks.

class Product:
    tax_rate=0.1
    def __init__(self, name, base_price):
        self.name=name
        self.base_price=base_price

    def final_price(self):
        return self.base_price+(self.base_price*Product.tax_rate)

    @classmethod
    def change_tax(cls, new_rate):
        cls.tax_rate=new_rate

    @staticmethod
    def is_valid_price(price):
        return 0 <= price < 100000


p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)
print(p1.name, p1.final_price())
print(p2.name, p2.final_price())

Product.change_tax(0.2)
print(p1.name, p1.final_price())
print(p2.name, p2.final_price())