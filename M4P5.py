#Input
fixed_costs = float(input("Enter fixed costs: "))
price_per_unit = float(input("Enter price per unit: "))
cost_per_unit = float(input("Enter cost per unit: "))

#Process
break_even_point = fixed_costs / (price_per_unit - cost_per_unit)

#Output
print(f"The break-even point is: {break_even_point} units")
