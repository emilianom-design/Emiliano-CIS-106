def compute_pay_rate(job_code):
    if job_code == 'L':
        return 25 
    elif job_code == 'A':
        return 30  
    elif job_code == 'J':
        return 50  
    else:
        return 0 

def pay_main():
    total_gross_pay = 0.0
    while True:
        last_name = input("Enter employee's last name (or 'done' to stop): ")
        if last_name.lower() == 'done':
            break

        job_code = input(f"Enter job code for {last_name} (L, A, J): ").upper()
        hours_worked = float(input(f"Enter hours worked by {last_name}: "))

        rate = compute_pay_rate(job_code)
        if rate == 0:
            print("Invalid job code entered. Please enter a valid job code.")
            continue

        if hours_worked > 40:
            regular_pay = 40 * rate
            overtime_pay = (hours_worked - 40) * (rate * 1.5)
            gross_pay = regular_pay + overtime_pay
        else:
            gross_pay = hours_worked * rate

        print(f"{last_name}'s gross pay is ${gross_pay:.2f}")
        total_gross_pay += gross_pay

    print(f"Total gross pay for all employees: ${total_gross_pay:.2f}")

pay_main()
