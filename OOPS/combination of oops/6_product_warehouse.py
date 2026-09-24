# 6. Create:
# • Product class with private price and quantity
# • Warehouse class containing multiple products
# • Overload:
# o + to merge warehouses
# o len() to return number of unique products
# o in operator to check if product exists
# • Provide class method to track total warehouses created
class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.__price = price
        self.__qty = qty
class Warehouse:
    count = 0
    def __init__(self, products):
        self.products = products
        Warehouse.count = Warehouse.count + 1
    def __add__(self, other):
        return Warehouse(self.products + other.products)
    def __len__(self):
        unique_names = set()
        for p in self.products:
            unique_names.add(p.name)
        return len(unique_names)
    def __contains__(self, item):
        for p in self.products:
            if p.name == item:
                return True
        return False
w1 = Warehouse([Product("A", 10, 5)])
w2 = Warehouse([Product("B", 20, 2)])
w3 = w1 + w2
print("Unique products:", len(w3))
print("Contains A:", "A" in w3)
