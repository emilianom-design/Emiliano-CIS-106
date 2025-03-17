def compute_tuition(credit_hours, district_code):
    if district_code == "I":
        return credit_hours * 250
    elif district_code == "O":
        return credit_hours * 550
    else:
        return 0

total_tuition = 0.0
decision = input("Do you want to run this program? enter yes ").lower()
while decision[0] == "y":
    last_name = input("enter student's last name ")
    district_code = input("enter 'I' if in district or 'O' if out of district ")
    credit_hours = int(input(f"how many credit hours are being taken by {last_name}: "))
    tuition = compute_tuition(credit_hours, district_code)

    
    print(f"{last_name}'s tuition owed is ${tuition}")
    total_tuition += tuition

    decision = input("Do you want to continue entering students? Enter 'yes' or 'no': ").lower()

print(f"Total tuition owed by all students: ${total_tuition:.2f}")

    
