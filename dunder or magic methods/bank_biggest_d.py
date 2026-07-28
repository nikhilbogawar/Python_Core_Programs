# Create a Bank class with account number, name , pin, and balance=0 as attributes
# b1 is Bank class object
# b1+30000 -> 30000 is deposited in to yor bank account
# b1-25000 -> 25000 is withdrawn        (use pin validation before performing operation) if wrong pin enter print invalid pin
# b1() -> display total details of your account   (use pin validation before performing operation) if wrong pin enter print invalid pin
# l=[b1,b2,b3]; print(l); -> [Names]
# b1>b2 -> checks using both accounts balance
# print(b1) -> display's details except pin   (use pin validation before performing operation) if wrong pin enter print invalid pin

class Bank:
    def __init__(self, acc_no, name, pin, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.__pin = pin
        self.balance = balance
    def __add__(self, amount):
        pin = int(input("Enter PIN for deposit: "))
        if pin == self.__pin:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Invalid PIN")
        return self
    def __sub__(self, amount):
        pin = int(input("Enter PIN for withdrawal: "))
        if pin == self.__pin:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn {amount}. New Balance: {self.balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid PIN")
        return self
    def __call__(self):
        pin = int(input("Enter PIN to view details: "))
        if pin == self.__pin:
            print(f"Account No: {self.acc_no}, Name: {self.name}, Balance: {self.balance}")
        else:
            print("Invalid PIN")
    def __repr__(self):
        return self.name
    def __gt__(self, other):
        return self.balance > other.balance
    def __str__(self):
        pin = int(input("Enter PIN to view account summary: "))
        if pin == self.__pin:
            return f"Account No: {self.acc_no}, Name: {self.name}, Balance: {self.balance}"
        else:
            return "Invalid PIN"

b1 = Bank(101, "Nikhil", 1234, 15000)
b2 = Bank(102, "Arjun", 4321, 13000)
b3 = Bank(103, "Raj", 1111, 10000)

b1 + 30000
b1 - 25000
b1()
b2 + 500
b2 - 2000
b2()
b3 + 4000
b3 - 2000
b3()
# print([b1, b2, b3])
# print(b1 > b2)
print(b1)
print(b2)
print(b3)