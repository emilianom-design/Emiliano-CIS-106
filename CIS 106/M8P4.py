items = [
    ("Laptop", 3, 800.00),
    ("Smartphone", 5, 450.00),
    ("Headphones", 10, 50.00),
    ("Mouse", 7, 25.00),
    ("Keyboard", 4, 75.00)
]

total_extended_price = 0.0
total_orders = 0

print(f"{'Item':<10}{'Quantity':<10}{'Price':<10}{'Extended Price':<15}")

for item, quantity, price in items:
    extended_price = quantity * price
    total_extended_price += extended_price
    total_orders += 1
    print(f"{item:<10}{quantity:<10}{price:,.2f}{extended_price:,.2f}")

average_order = total_extended_price / total_orders if total_orders else 0.0
print(f"Total extended prices: ${total_extended_price:,.2f}")
print(f"Number of orders: {total_orders}")
print(f"Average order value: ${average_order:,.2f}")
