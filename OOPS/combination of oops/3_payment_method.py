# 3. Create:
# • Abstract class PaymentMethod with pay(), validate()
# • Subclasses: CardPayment, WalletPayment, UPIPayment
# • Encapsulate user balance
# • Use @property to control reading available funds
# • Overload + operator to combine two payment methods into “split payment”
# • Demonstrate polymorphism through a checkout loop.
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    def __init__(self,balance):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    @abstractmethod
    def pay(self,amount):
        pass
    def validate(self,amount):
        if amount<=self.__balance:
            return True
        else:
            return False
    def __add__(self, other):
        split=SplitPayment([self,other])
        return split
class CardPayment(PaymentMethod):
    def pay(self,amount):
        return self.validate(amount)
class WalletPayment(PaymentMethod):
    def pay(self,amount):
        return self.validate(amount)
class UPIPayment(PaymentMethod):
    def pay(self,amount):
        return self.validate(amount)
class SplitPayment(PaymentMethod):
    def __init__(self, methods):
        # super().__init__(balance)
        self.methods=methods
    def pay(self,amount):
        for m in self.methods:
            if not m.pay(amount/len(self.methods)):
                return False
        return True
c=[CardPayment(300),WalletPayment(500),UPIPayment(600)]
for i in c:
    result=i.pay(200)
    print(result)