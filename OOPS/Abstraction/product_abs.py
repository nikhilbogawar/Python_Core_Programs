from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price
    @abstractmethod
    def order(self):
        print("ordering product")
    @abstractmethod
    def delivery(self):
        print("Delivery product")
print(Product.__abstractmethods__)
class Iphone(Product):
    def __init__(self,name,price):
        Product.__init__(self,name,price)
    def order(self):
        print("ordering Iphone")
    def delivery(self):
        print("Iphone delivered")
print(Iphone.__abstractmethods__)
