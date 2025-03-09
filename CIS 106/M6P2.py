#input
part_number = input("Enter part number: ")
quantity = int(input("Enter quantity: "))
if part_number == "10" or part_number == "55": unit_cost = 1.00
elif part_number == "99": unit_cost = 2.00
elif part_number == "80" or part_number == "70": unit_cost = 3.00
else: unit_cost = 5.00
#Process
total_cost = quantity * unit_cost
#output
print(f"Part number: {part_number}")
print(f"Cost per unit: ${unit_cost}")
print(f"Total cost: ${total_cost}")
