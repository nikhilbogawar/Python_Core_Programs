# Create a Bank class with account number, name , pin, and balance=0 as attributes
# b1 is Bank class object
# b1+30000 -> 30000 is deposited in to yor bank account
# b1-25000 -> 25000 is withdrawn        (use pin validation before performing operation) if wrong pin enter print invalid pin
# b1() -> display total details of your account   (use pin validation before performing operation) if wrong pin enter print invalid pin
# l=[b1,b2,b3]; print(l); -> [Names]
# b1>b2 -> checks using both accounts balance
# print(b1) -> display's details except pin   (use pin validation before performing operation) if wrong pin enter print invalid pin

class Bank:
    def __init__(self, name, pin, acc):
        self.name=name
        self.acc=acc
        self.balance=0
        self.pin=pin
