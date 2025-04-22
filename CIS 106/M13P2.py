student_grades = {
    "Alice": [85, 90, 88],
    "Bob": [92, 89, 95],
    "Charlie": [78, 80, 82],
    "Diana": [90, 91, 94],
    "Ethan": [88, 84, 86]
}

def compute_averages(grades_dict):
    avg_list = []
    for name, grades in grades_dict.items():
        avg = sum(grades) / len(grades)
        avg_list.append([name, avg])
    return avg_list

averages = compute_averages(student_grades)

print(f"{'Student':<10} {'Average':<6}")
print("-" * 20)
for name, avg in averages:
    print(f"{name:<10} {avg:.2f}")

grade_totals = [0, 0, 0]
for grades in student_grades.values():
    for i in range(3):
        grade_totals[i] += grades[i]

print("\nClass average per assignment:")
for i, total in enumerate(grade_totals):
    print(f"Assignment {i+1}: {total / len(student_grades):.2f}")
