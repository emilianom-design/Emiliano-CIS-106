employees = [
    ("jackson", 40000.00),
    ("parker", 70000.00),
    ("reid", 25000.00),
    ("banner", 70000.00),
    ("stark", 900000.00)
]

total_bonus = 0.0
print(f"{'Last Name':<10}{'Salary':<10}{'Bonus':<10}")

for last_name, salary in employees:
    if salary >= 100000:
        bonus_rate = 0.30
    elif salary >= 50000:
        bonus_rate = 0.25
    else:
        bonus_rate = 0.15
    
    bonus = salary * bonus_rate
    total_bonus += bonus
    print(f"{last_name:<10}{salary:,.2f}{bonus:,.2f}")

print(f"Total bonuses paid out: ${total_bonus:,.2f}")
