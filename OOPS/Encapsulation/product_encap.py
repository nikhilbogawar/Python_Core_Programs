# 5. Create a Product class where:
# • price cannot be negative
# • discount cannot exceed 70%
# • internal final price calculation should not be directly exposed
# Provide only one public method get_final_price().

class Product:
    def __init__(self,price,discount):
        if price<0 or discount>70:
            print("Invalid Price or Discount")
        self.__price=price
        self.__discount=discount
    def get_final_price(self):
        return self.__price*(1-self.__discount/100)
p=Product(599,15)
print(p.get_final_price())