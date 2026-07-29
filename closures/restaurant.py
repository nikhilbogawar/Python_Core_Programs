# Write a function restaurant(food_item).
#
# -   The outer function stores the food item.
# -   The inner function receives the quantity.
# -   Print the order details.
# -   Return the inner function.
def restaurant(food_item):
    def food(quantity):
        return f"Food Item : {food_item}\nQuantity : {quantity}"
    return food
f1=restaurant("Biryani")
print(f1(2))