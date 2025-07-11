print("hello")
def calculate_total(price, quantity):
    total = price + quantity  # ❌ Logic error: should be price * quantity
    return total

item_price = 100
item_quantity = 3
final_amount = calculate_total(item_price, item_quantity)

print("Total Amount:", final_amount)