# Create a class BankAccount with:
# •	class variable bank_name
# •	instance variables holder and balance
# •	instance method deposit(amount)
# •	class method change_bank_name(cls, new_name)
# •	static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.

class BankAccount:
    bank_name = "SBI"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print("Deposited:", amount, "New Balance:", self.balance)
        else:
            print("Invalid amount")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount):
        return amount > 0

print("Current Bank Name:", BankAccount.bank_name)
acc1 = BankAccount("Nikhil", 1000)
acc1.deposit(500)

BankAccount.change_bank_name("BOB")
print("Changed Bank Name:", BankAccount.bank_name)
