# Write a function shopping_cart(item_name).
#
# -   The outer function receives the item name.
# -   The inner function receives:
#     -   quantity
#     -   price per item
# -   Print the item name, quantity, and total price.
# -   Return the inner function.
def shopping_cart(item_name):
    def inner(quantity, price_per_item):
        total=quantity*price_per_item
        print(f"Item Name : {item_name} | Quantity : {quantity} | Total Price : {total}")
        return total
    return inner
s1=shopping_cart("T-shirts")
s1(2,249)