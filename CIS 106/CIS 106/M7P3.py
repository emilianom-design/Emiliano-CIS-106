student_count = 0
#input
user_input = input("Do you want to proceed with program? (Yes/No): ").strip().lower()

while user_input == "yes":
    last_name = input("Enter the student's last name: ")
    score1 = float(input("Enter the first exam score: "))
    score2 = float(input("Enter the second exam score: "))
    
    # Calculate the average score
    average_score = (score1 + score2) / 2
    
    # Display the student's last name and average score
    print(f"{last_name}, your average score is: {average_score:.2f}")
    print(f"Number of students who entered data: {student_count}")
    student_count += 1
    
    user_input = input("Do you want to run this program again? (Yes/No): ").strip().lower()
