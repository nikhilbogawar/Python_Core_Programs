# Build a payment system with a base class Payment(amount) and three subclasses: CreditCard, UPI, and NetBanking.
# Each overrides a method process() with its own logic. Write a function checkout(payment) that calls process()
# on any payment object and demonstrate polymorphism.
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        return f"Processing payment of {self.amount}"


class CreditCard(Payment):
    def process(self):
        return f"Paid {self.amount} using Credit Card"


class UPI(Payment):
    def process(self):
        return f"Paid {self.amount} using UPI"


class NetBanking(Payment):
    def process(self):
        return f"Paid {self.amount} using NetBanking"


def checkout(payment):
    print(payment.process())


checkout(CreditCard(500))
checkout(UPI(300))
checkout(NetBanking(1000))
