def calculate_scores(exam1, exam2, exam3):
    total_points = exam1 + exam2 + exam3
    average_score = total_points / 3
    return total_points, average_score

def main():
    last_name = input("Enter student's last name: ")
    exam1 = float(input("Enter first exam score: "))
    exam2 = float(input("Enter second exam score: "))
    exam3 = float(input("Enter third exam score: "))
    
    total_points, average_score = calculate_scores(exam1, exam2, exam3)
    
    print(f"Student: {last_name}")
    print(f"Total points: {total_points}")
    print(f"Average score: {average_score:.2f}")

if __name__ == "__main__":
    main()
