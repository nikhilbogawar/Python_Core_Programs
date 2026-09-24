# 1. Design a banking system with:
# • An abstract base class Account with deposit(), withdraw(),
# calculate_interest().
# • Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount.
# • Each account must:
# o Encapsulate balance (private)
# o Provide controlled access through properties
# o Override interest calculation differently
# • Include a static method to validate amount.
# • Include a class method to update bank-wide interest policies.
# Demonstrate:
# • Polymorphic behavior by iterating through all account types
# • Preventing direct access to balance
# • Multiple interest strategies

from abc import ABC, abstractmethod
class Account(ABC):
    interest_rate=0.08
    def __init__(self,balance=0):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    def deposit(self,amount):
        if self.validate_amount(amount):
            self.__balance=self.__balance+amount
        else:
            print('Invalid deposit amount')
    def withdraw(self,amount):
        if self.validate_amount(amount):
            if amount<=self.__balance:
                self.__balance=self.__balance-amount
            else:
                print("Insufficient funds")
        else:
            print("Invalid withdrawal amount")
    @abstractmethod
    def calculate_interest(self):
        pass
    @staticmethod
    def validate_amount(amount):
        if amount>0:
            return True
        else:
            return False
    @classmethod
    def update_policy(cls,rate):
        cls.interest_rate=rate
class SavingsAccount(Account):
    def calculate_interest(self):
        return self.balance*self.interest_rate
class CurrentAccount(Account):
    def calculate_interest(self):
        return self.balance*self.interest_rate
class FixedDepositAccount(Account):
    def calculate_interest(self):
        return self.balance*self.interest_rate
a=[SavingsAccount(1000),CurrentAccount(2000),FixedDepositAccount(5000)]
for i in a:
    print(type(i).__name__,i.calculate_interest())