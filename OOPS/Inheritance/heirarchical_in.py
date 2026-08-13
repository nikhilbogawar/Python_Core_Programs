class User:
    def __init__(self,n,a,g,dob):
        self.name=n
        self.age=a
        self.gender=g
        self.dob=dob

    def login(self):
        print("Login successful")

    def logout(self):
        print("Logout successful")

class Restaurants:
    def __init__(self,name,address,rating):
        self.name=name
        self.address=address
        self.rating=rating

    def display_menu(self):
        print("All dishes are veg only")

class Swiggy(User, Restaurants):
    def display(self):
        print("User details")
print(Swiggy.mro())

class Zomato(User, Restaurants):
    def display(self):
        print("User1 details")

class Customer(Swiggy,Zomato):
    def order(self):
        print("Just Ordering")
print(Customer.mro())

s1=Zomato("Nikhil",21,"Male","15 Jan 2005")
s1.login()
s1.logout()
s1.display_menu()
s1.display()
