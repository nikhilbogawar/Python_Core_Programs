class CoffeeMachine:
    def __init__(self,brand,coffee_type,price,cups_available):
        self.brand=brand
        self.coffee_type=coffee_type
        self.price=price
        self.cups_available=cups_available
    def make_coffee(self):
        self.cups_available-=1
        print(f"No of cups remaining : {self.cups_available}")
    def refill_cups(self,quantity):
        self.cups_available+=quantity
        print(f"adding more quantity : {self.cups_available}")
    def display_details(self):
        print(f"Brand : {self.brand} | Coffee Type : {self.coffee_type} | Price : {self.price}")
    def __str__(self):
        return "This is our Coffee Cafe taste it and enjoy your free time"
    def __len__(self):
        return f"length : {self.cups_available}"
    def __add__(self, other):
        n=self.cups_available+other.cups_available
        return f"combine of available cups from two coffee machine objects : {n}"
c1=CoffeeMachine("Starbucks","Sugarless",1500,10)
c2=CoffeeMachine("Normal brand","pulpy",300,5)
c1.make_coffee()
c2.make_coffee()
c1.refill_cups(10)
c1.display_details()
print(c1.__str__())
print(c1.__len__())
print(c1.__add__(c2))