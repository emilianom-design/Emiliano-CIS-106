#Input
item = input("Enter the item (A or B): ")
quantity = int(input("Enter the quantity: "))    
if item == "A": unit_price = 10.00
else: unit_price = 20.00

#Process
extended_price = unit_price * quantity

#Output
print(f"Item: {item}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")
