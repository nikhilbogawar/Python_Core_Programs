# 1. Bank Management System
# Create a Bank class with:
# • balance variable
# • deposit()
# • withdraw()
# • check_balance()
# Create a User class that inherits Bank and displays the user's name. Perform
# deposit, withdrawal, and balance check.
class Bank:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdrawal or insufficient balance")
    def check_balance(self):
        print(f"Current Balance: {self.balance}")
class User(Bank):
    def __init__(self, name, balance=0):
        super().__init__(balance)
        self.name = name
    def display_user(self):
        print(f"User: {self.name}")
u1 = User("Nikhil", 5000)
u1.display_user()
u1.deposit(2000)
u1.withdraw(3000)
u1.check_balance()
