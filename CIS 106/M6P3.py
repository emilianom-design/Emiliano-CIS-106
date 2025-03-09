#input
principle = float(input("Enter the principle amount of the CD: "))
years = int(input("Enter the years to maturity: "))
if principle > 100000 and years == 5: interest_rate = 0.06
elif 50000 <= principle <= 100000 and years == 10: interest_rate = 0.05
elif 50000 <= principle <= 100000 and years == 5: interest_rate = 0.04
else: interest_rate = 0.02
#Process
interest_amount = principle * interest_rate
#Output
print(f"Principle: ${principle}")
print(f"Interest Rate: {interest_rate * 100}%")
print(f"First Year Interest: ${interest_amount}")
