#Input
appliance_name = input("\nEnter the appliance name: ")
appliance_cost = float(input("Enter the cost of the appliance: "))
if appliance_cost > 1000: warranty_cost = appliance_cost * 0.10
else: warranty_cost = appliance_cost * 0.05

#Process total cost (appliance cost + warranty cost)
total_cost = appliance_cost + warranty_cost

#Output appliance details, warranty cost, and total cost
print(f"Appliance: {appliance_name}, Cost: ${appliance_cost:.2f}, Warranty Cost: ${warranty_cost:.2f}, Total Cost: ${total_cost:.2f}")
