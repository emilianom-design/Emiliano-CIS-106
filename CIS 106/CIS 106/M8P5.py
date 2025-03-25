students = [
    ("Martinez", "I", 15),
    ("Connor", "O", 18),
    ("Chang", "I", 12),
    ("Williams", "O", 14),
    ("Davis", "I", 20)
]

total_tuition = 0.0
total_students = len(students)

print(f"{'Last Name':<10}{'Credits':<10}{'Tuition Owed':<15}")

for last_name, district_code, credits in students:
    if district_code == "I":
        tuition = credits * 250.00
    else:
        tuition = credits * 500.00
    
    total_tuition += tuition
    print(f"{last_name:<10}{credits:<10}{tuition:,.2f}")

print(f"Total tuition owed: ${total_tuition:,.2f}")
print(f"Number of students: {total_students}")
