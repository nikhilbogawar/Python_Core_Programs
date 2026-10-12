# 6. Create a class in a module that uses private attributes and @property /
# @setter decorators. Import the class into another module and show how
# encapsulation protects the data while still allowing controlled access.
from account import Account
a=Account(10000)
print(a.balance)

a.balance=80000
print(a.balance)