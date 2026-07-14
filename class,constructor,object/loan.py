# Build a Loan class that:
# •	Has a common interest rate for all loans.
# •	Each object stores borrower name and principal.
# •	Calculates total payable amount.
# •	Provides a function to update the interest rate.
# •	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
# Demonstrate:
# 1.	Creating multiple loan accounts.
# 2.	Updating interest rates.
# 3.	Checking eligibility and total repayment for borrowers.

class Loan:
    interest_rate = 0.1

    def __init__(self, borrower, principal):
        self.borrower = borrower
        self.principal = principal

    def total_payable(self):
        return self.principal + (self.principal * Loan.interest_rate)

    @classmethod
    def update_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @staticmethod
    def is_eligible(salary):
        return salary >= 20000

l1 = Loan("Nikhil", 100000)
l2 = Loan("Nicky", 50000)
print(l1.borrower, l1.total_payable())
print(l2.borrower, l2.total_payable())

Loan.update_rate(0.2)
print(l1.borrower, l1.total_payable())
print(Loan.is_eligible(15000))