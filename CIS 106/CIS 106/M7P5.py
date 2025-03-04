total_discount = 0

# input
continue_program = input("Do you want to run the program? (Yes/No): ").strip().lower()

while continue_program == 'yes':
    quantity = int(input("Enter quantity amount: "))
    price = float(input("Enter the price of the item: "))

    # process
    extended_price = quantity * price
    if extended_price > 10000.00: 
        discount_percent = 25.0
    else:
        discount_percent = 10.0

    discount_amount = extended_price * (discount_percent / 100) 
    total = extended_price - discount_amount

    # output
    print(f"The extended price is: ${extended_price:.2f}")
    print(f"The discount amount is: ${discount_amount:.2f}")
    print(f"The total is: ${total:.2f}")

    total_discount += discount_amount

    continue_program = input("Do you want to run the program again? (Yes/No): ").strip().lower()

print(f"Total discount amount for all orders: ${total_discount:.2f}")
