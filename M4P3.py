#Input
meal_total = float(input("Enter the total for the meal: $"))

#process phase
tip_15 = meal_total * 0.15
total_15 = meal_total + tip_15
tip_18 = meal_total * 0.18
total_18 = meal_total + tip_18
tip_20 = meal_total * 0.20
total_20 = meal_total + tip_20

#output
print(f"\nWith 15% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip_15:.2f}")
print(f"Total with Tip: {total_15:.2f}")
print()
print(f"With 18% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip_18:.2f}")
print(f"Total with Tip: {total_18:.2f}")
print()
print(f"With 20% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip_20:.2f}")
print(f"Total with Tip: {total_20:.2f}")
