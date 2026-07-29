# Write a function discount(percent).
#
# -   The outer function receives the discount percentage.
# -   The inner function receives the product price.
# -   Print the final price after applying the discount.
# -   Return the inner function.
def discount(percent):
    def product(price):
        total=price-(price*percent/100)
        print(total)
        return total
    return product
d1=discount(10)
d1(1000)