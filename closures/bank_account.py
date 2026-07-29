# Write a function bank_account(balance).
#
# -   The outer function receives the initial balance.
# -   The inner function receives an amount to withdraw.
# -   Print the remaining balance.
# -   Return the inner function.
def bank_account(balance):
    def amount(withdraw):
        if balance>=withdraw:
            total=balance-withdraw
            print(total)
            return total
        else:
            print("Insufficient Balance")
    return amount
b1=bank_account(1500)
b1(1500)