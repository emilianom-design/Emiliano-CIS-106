#input phase
Quantity = float(input("input quantity of item"))

if Quantity >= 1000: unit_price = 3.00
else: unit_price = 5.00

#Process phase
Extended_price = unit_price * Quantity
tax = Extended_price * 0.07
Total = Extended_price + tax

#Output phase
print(f"Quantity: {Quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${Extended_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${Total:.2f}")
