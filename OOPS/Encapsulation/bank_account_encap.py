# 1.  Create a BankAccount class that stores:
# • account number
# • balance (should not be directly modifiable)
# You must:
# 1. Make the balance attribute inaccessible from outside.
# 2. Provide functions to deposit/withdraw that validate the amount.
# 3. Prevent withdrawal if balance becomes negative.
# 4. Show what happens if someone tries to modify balance directly and why
# encapsulation prevents it.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self. account_number=account_number
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("Invalid Deposit")
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
a1=BankAccount("656655",10000)
a1.deposit(500)
a1.withdraw(1000)
print(a1.get_balance())
a1.__balance=10000   # a1._BankAccount__balance=10000 (then it works)
print(a1.get_balance())