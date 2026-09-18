# 8. Create a ShoppingCart class where:
# • items are stored privately
# • users cannot directly modify item list
# • only add/remove methods are allowed
# • provide a method to get a safe copy of the cart items (not direct reference to internal
# list)

# class ShoppingCart:
#     def __init__(self):
#         self.__items=[]
#     def add_item(self,item):
#         self.__items.append(item)
#     def remove_item(self,item):
#         if item in self.__items:
#             self.__items.remove(item)
#     def get_items(self):
#         return list(self.__items)
# c=ShoppingCart()
# c.add_item("Choco Chips")
# c.add_item("Kinder Joy")
# c.add_item("Mango Bite")
# print(c.get_items())
# items=c.get_items()
# items.append("5 Star")  # modifies copy only
# print(c.get_items())
# c.remove_item("Mango Bite")
# print(c.get_items())


# for this answer adding something crazy:------>>>>> sir method
class ShoppingCart:
    def __init__(self):
        self.__items=[]
    def __add__(self, p):
        self.__items.append(p)
    def __sub__(self, p):
        self.__items.remove(p)
    def get_cart(self):
        return self.__items.copy()
c1=ShoppingCart()
c1+"Iphone"
c1+"Laptop"
c1+"Tab"
c1-"Tab"
print(c1.get_cart())