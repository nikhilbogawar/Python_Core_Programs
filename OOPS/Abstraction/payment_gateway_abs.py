# 12. Design an abstract class PaymentGateway with:
# • authenticate()
# • pay(amount)
# • refund(amount)
# Implement subclasses:
# • UPIPayment
# • CardPayment
# • NetBankingPayment
# Show how abstraction helps your main program call payment methods without caring about
# the payment type.

from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self):
        pass
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass
class UPIPayment(PaymentGateway):
    def authenticate(self):
        print("upi authenticated")
    def pay(self,amount):
        print(f"paid {amount} using upi")
    def refund(self,amount):
        print(f"refunded using upi")
class CardPayment(PaymentGateway):
    def authenticate(self):
        print("card authenticated")
    def pay(self,amount):
        print(f"paid {amount} using card")
    def refund(self,amount):
        print("refunded using card")
class NetBankingPayment(PaymentGateway):
    def authenticate(self):
        print("net banking authenticated")
    def pay(self,amount):
        print(f"paid {amount} using net banking")
    def refund(self,amount):
        print("refunded using net banking")
def process_payment(pg: PaymentGateway):
    pg.authenticate()
    pg.pay(100)
    pg.refund(50)
p=[UPIPayment(), CardPayment(), NetBankingPayment()]
for i in p:
    process_payment(i)