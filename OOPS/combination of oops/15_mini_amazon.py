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

# sir method:--->>>>>>>>
# from abc import ABC, abstractmethod
# class User(ABC):
#     total_users = 0
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age
#         self.total_users += 1
#     @abstractmethod
#     def get_role(self):
#         pass
#     @classmethod
#     def get_total_users(cls):
#         return cls.total_users
# class Product:
#     def _init_(self, name, price):
#         self.name = name
#         self.price = price
#     def _repr_(self):
#         return f'Product({self.name}, {self.price})'
#     def _str_(self):
#         return f'Product({self.name}, {self.price})'
# class Seller(User):
#     def _init_(self, name, age):
#         super()._init_(name, age)
#     def get_role(self):
#         return "seller"
# class Buyer(User):
#     def _init_(self, name, age, cart):
#         super()._init_(name, age)
#         self.cart = cart
#     def get_role(self):
#         return "buyer"
#     def checkout(self):
#         print(f"{self.cart.get_totalprice()} is the total price")
# class Order:
#     def _init_(self, product, quantity):
#         self.product = product
#         self.quantity = quantity
# class Reward:
#     def get_totalprice(self, tp):
#         if tp > 1000:
#             return tp * 0.9
#         return tp
# class Cart(Reward):
#     def _init_(self):
#         self.__cart = []
#     def _add_(self, other):
#         self.__cart.append(other)
#     def _sub_(self, other):
#         self.__cart.remove(other)
#     def get_cart(self):
#         return self.__cart.copy()
#     def get_totalprice(self):
#         tp = 0
#         for i in self.__cart:
#             tp += i.price
#         return super().get_totalprice(tp)
#     def checkout(self, role, total_price):
#         if role == "seller":
#             print(f"Checkout with price {total_price} received")
#         else:
#             print(f"Checkout with price {total_price} paid")
# def checkout(user, cart):
#     total_price = cart.get_totalprice()
#     cart.checkout(user.get_role(), total_price)
# product = Product("laptop", 100)
# c = Cart()
# c + product
# p = Product("AC", 300)
# c + p
# print(c.get_cart())
# print(c.get_totalprice())
# u2 = Buyer("B", 30, c)
# u2.checkout()