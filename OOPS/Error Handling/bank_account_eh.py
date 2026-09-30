# • Create a class BankAccount with an attribute balance.
# Implement a method withdraw(amount) that raises an exception
# if the withdrawal amount is greater than the available balance.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient balance")
        self.balance -= amount
        print("Withdrawal successful")
        print("Remaining balance:", self.balance)
account = BankAccount(5000)
try:
    account.withdraw(6000)
except Exception as e:
    print("Error:", e)