#Input
tickets = int(input("Enter number of concert tickets: "))
if tickets >= 25: price_per_ticket = 50
elif 10 <= tickets <= 24: price_per_ticket = 60
elif 5 <= tickets <= 9: price_per_ticket = 70
else: price_per_ticket = 75
#Process
total_cost = tickets * price_per_ticket
#Output
print(f"Number of tickets: {tickets}")
print(f"Price per ticket: ${price_per_ticket}")
print(f"Total cost: ${total_cost}")
