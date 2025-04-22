student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Ethan": 88
}

print(f"{'Student':<10} {'Grade':<5}")
print("-" * 20)
total = 0
for name, grade in student_grades.items():
    print(f"{name:<10} {grade:<5}")
    total += grade

class_avg = total / len(student_grades)
print(f"\nClass Average: {class_avg:.2f}")
