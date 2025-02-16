#Input
last_name = input("\nEnter your last name: ")
dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter your gross income: "))

# Process phase
adjusted_gross_income = gross_income - (dependents * 12000)
if adjusted_gross_income > 50000: tax_rate = 0.20
else: tax_rate = 0.10
income_tax = adjusted_gross_income * tax_rate
if income_tax < 0: income_tax = 100

#Output the results
print(f"\nLast Name: {last_name}, Gross Income: ${gross_income:.2f}, Number of Dependents: {dependents}, "
      f"Adjusted Gross Income: ${adjusted_gross_income:.2f}, Income Tax: ${income_tax:.2f}")
