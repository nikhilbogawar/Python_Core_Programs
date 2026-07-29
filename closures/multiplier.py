# Write a function multiplier(number).
#
# -   The outer function receives one number.
# -   The inner function receives another number.
# -   Print their multiplication.
# -   Return the inner function.
def multiplier(number):
    def mul(number2):
        total=number*number2
        print(total)
        return total
    return mul
m1=multiplier(12)
m1(5)