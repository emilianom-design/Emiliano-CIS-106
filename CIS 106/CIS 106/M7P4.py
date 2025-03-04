total_gross_pay = 0
employee_count = 0
    
# input
continue_program = input("Do you want to run the program? (Yes/No): ").strip().lower()
    
while continue_program == 'yes':
    last_name = input("Enter employee's last name: ")
    hours_worked = float(input("Enter hours worked: "))
    rate_of_pay = float(input("Enter rate of pay: "))
        
    # process   
    if hours_worked > 40: 
        overtime_hours = hours_worked - 40
        gross_pay = (40 * rate_of_pay) + (overtime_hours * rate_of_pay * 1.5)
    else: 
        gross_pay = hours_worked * rate_of_pay
        
    # output  
    print(f"{last_name}: Gross Pay: ${gross_pay:.2f}")
        
    total_gross_pay += gross_pay
    employee_count += 1
        
    # Checking for employees count after processing
    if employee_count > 0: 
        average_pay = total_gross_pay / employee_count
        print(f"Total gross pay for all employees: ${total_gross_pay:.2f}")
        print(f"Number of employees: {employee_count}")
        print(f"Average pay: ${average_pay:.2f}")
    else: 
        print("No employees were entered.")

    continue_program = input("Do you want to enter another employee? (Yes/No): ").strip().lower()

