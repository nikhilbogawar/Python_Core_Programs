# 4. Food Ordering System Using Multilevel Inheritance
# Class 1: Restaurant
# • Create a method menu(item) that returns the price of the selected food
# item.
# Class 2: FoodCourt (inherits Restaurant)
# Create the following methods:
# • display_menu() – Display the available food items.
# • order() – Accept the food item from the user and allow multiple orders.
# • billing() – Display the total bill and add a packing charge of ₹20.
# Class 3: Customer (inherits FoodCourt)
# • Create an object of the Customer class.
# • Call the order() method.
class Restaurant:
    menu_items={"Pizza":149,"Burger":69,"Pasta":99,"Sandwich":49,"Coffee":39}
    def menu(self,item):
        return self.menu_items.get(item, None)
class FoodCourt(Restaurant):
    def __init__(self):
        self.orders=[]
    def display_menu(self):
        print("---------Menu----------")
        for item, price in self.menu_items.items():
            print(f"{item}:{price}rs")
        print("-----------------------")
    def order(self):
        while True:
            item=input("Enter food item (or 'done' to finish): ")
            if item.lower()=="done":
                break
            if self.menu(item) is not None:
                self.orders.append(item)
                print(f"{item} added to the order")
            else:
                print("Item not available..! Please choose from menu")
    def billing(self):
        total=sum(self.menu(item) for item in self.orders)
        total+=20
        print("----------Bill----------")
        for item in self.orders:
            print(f"{item}: {self.menu(item)}rs")
        print("Packing Charge: 20rs")
        print(f"Total Amount: {total}rs")
        print("------------------------")
class Customer(FoodCourt):
    def __init__(self,name):
        super().__init__()
        self.name=name
c1=Customer("Nikhil")
c1.display_menu()
c1.order()
c1.billing()