class ShoppingCart:
    def __init__(self):
        self.cart=[]

    def __add__(self, other):
        self.cart.append(other)
        return self.cart

c1=ShoppingCart()
c2=ShoppingCart()
print(c1+"chocolates")