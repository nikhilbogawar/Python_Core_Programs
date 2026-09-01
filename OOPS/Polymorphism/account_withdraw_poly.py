# Q8. Create:
# • Base Account → withdraw()
# • Subclass SavingsAccount → modifies withdraw()
# • Subclass PremiumSavingsAccount → overrides again but calls parent using super()
# Show how polymorphism works across multiple levels.
class Account:
    def withdraw(self,amount):
        print(f"Withdrawing {amount} from Account")
class SavingsAccount(Account):
    def withdraw(self,amount):
        print("Savings Account")
        print(f"Check limit before withdrawing {amount}")
class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self,amount):
        print("Premium Savings Account")
        super().withdraw(amount)
        print(f"Extra benefits applied {amount}")
a1=Account()
a1.withdraw(100)
s1=SavingsAccount()
s1.withdraw(200)
p1=PremiumSavingsAccount()
p1.withdraw(500)