# 15.
# Classes:
# • User
# Create a mini version of Amazon with:
# • Product
# • Seller(User)
# • Buyer(User)
# • Order
# • Cart
# Requirements (must use all OOP concepts):
# >Inheritance: Seller and Buyer extend User
# >Encapsulation: protect internal cart list, user password
# >Abstraction: base class User defines abstract get_role()
# >Polymorphism: different users behave differently in checkout
# >Composition: Buyer “has” a Cart
# >Operator overloading:
# • + to add product to Cart
# • - to remove product
# >Properties: validate product price
# >Class methods: tracking total users
# >Static methods: validating product IDs
# >__str__ for readable summaries
# >MRO behavior when Buyer inherits from multiple mixins (e.g., RewardsMixin)
from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    @abstractmethod
    def get_role(self):
        pass
class Seller(User):
    def get_role(self):
        return "Seller"
class Buyer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.cart = Cart()
    def get_role(self):
        return "Buyer"
    def checkout(self):
        print("Buyer checking out cart")
        print("Total:", self.cart.total())
class Product:
    def __init__(self, name, price):
        if price > 0:
            self.__price = price
        else:
            self.__price = 0
        self.name = name
    @property
    def price(self):
        return self.__price
class Cart:
    def __init__(self):
        self.__items = []
    def __add__(self, product):
        self.__items.append(product)
        return self
    def __sub__(self, product):
        if product in self.__items:
            self.__items.remove(product)
        return self
    def total(self):
        total_price = 0
        for item in self.__items:
            return total_price + item.price
    def __str__(self):
        names = [item.name for item in self.__items]
        return "Cart contains: " + ", ".join(names)
buyer1 = Buyer("Nikhil", "pass123")
p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)
buyer1.cart = buyer1.cart + p1
buyer1.cart = buyer1.cart + p2
print(buyer1.cart)
buyer1.checkout()

class RewardsMixin:
    def get_rewards(self):
        return "Rewards applied"
class BuyerWithRewards(Buyer, RewardsMixin):
    def get_role(self):
        return "Buyer with Rewards"
buyer2 = BuyerWithRewards("Ravi", "secure123")
print("Role:", buyer2.get_role())
print("MRO:", BuyerWithRewards.mro())
