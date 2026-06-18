# Write a function discount_price(price, discount=10) that returns the discounted price. Test with and without the discount argument. 
def discount_price(price, discount=10):
    discounted_price = price - (price * discount / 100)
    return discounted_price
print(discount_price(100))