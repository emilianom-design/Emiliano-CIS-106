#input
quantity = int(input("Enter quantity of widgets"))

#process phase
if quantity > 10000: price = 10.
elif 5000 <= quantity >= 10000: price = 20.
else: price = 30.
extended_price = quantity * price
tax_amount = extended_price * .07
total = extended_price + tax_amount

#output
print(f"Extended price: ${extended_price:.2f}, Tax amount: ${tax_amount:.2f}, Total: ${total:.2f}")
