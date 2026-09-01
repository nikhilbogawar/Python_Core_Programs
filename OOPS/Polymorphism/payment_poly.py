# Q6. Design:
# • Base class Payment with process(amount)
# • Subclass CreditCardPayment adds process(amount, card_type)
# Demonstrate what happens when overriding with different signatures and how Python
# handles it.
class Payment:
    def process(self,amount):
        print("payment successful")
        print(f"{amount} is paid")
class CreditCardPayment(Payment):
    def process(self,amount,card_type):
        print(f"{card_type} is used")
        super().process(amount)
p1=Payment()
p1.process(200)
c1=CreditCardPayment()
c1.process(2000,"Visa")