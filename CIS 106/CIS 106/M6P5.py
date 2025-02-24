#Input
last_name = input("Enter employee's last name: ")
salary = float(input("Enter employee's salary: "))
job_level = int(input("Enter job level: "))
if job_level >= 10: bonus_rate = 0.25
elif 5 <= job_level <= 9: bonus_rate = 0.20
else: bonus_rate = 0.10
#Process
bonus = salary * bonus_rate
#Output
print(f"Employee: {last_name}")
print(f"Bonus: ${bonus}")
