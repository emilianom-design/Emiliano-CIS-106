principle = float(input("Enter principle amount: "))
interest_rate = float(input("Enter interest rate: "))

total_interest = 0.0

print(f"{'Year':<6}{'Beginning Balance':<20}{'Ending Balance':<20}")

for year in range(1, 6):
    interest = principle * interest_rate
    total_interest += interest
    ending_balance = principle + interest
    print(f"{year:<6}{principle:,.2f}{ending_balance:,.2f}")
    principle = ending_balance  # Update principle for the next year

print(f"Total interest earned: ${total_interest:,.2f}")
