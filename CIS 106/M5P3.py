#Input
Number_of_books = int(input("\nEnter the number of books to order: "))
Cost_per_book = float(input("Enter the cost per book: "))

#Process
order_total = Number_of_books * Cost_per_book
if order_total > 50.00: shipping_charge = 0.00
else: shipping_charge = 25.00


#Output order total and shipping charge
print(f"Order Total: ${order_total:.2f}, Shipping Charge: ${shipping_charge:.2f}")
