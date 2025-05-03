class Student:
    district_rates = {
        "I": 250.00,
        "O": 500.00,
        "X": 800.00,
        "G": 250.00
    }

    def __init__(self, first, last, district_code, enrolled_credits):
        self.first = first
        self.last = last
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        rate = self.district_rates.get(self.district_code, 500.00)
        return self.enrolled_credits * rate

student_in = Student('Alice', 'Smith', 'I', 12)
student_out = Student('Bob', 'Jones', 'O', 15)
student_intl = Student('Carlos', 'Gomez', 'X', 9)
student_recip = Student('Diana', 'Lee', 'G', 6)

print(student_in.first, student_in.last, student_in.compute_tuition())
print(student_out.first, student_out.last, student_out.compute_tuition())
print(student_intl.first, student_intl.last, student_intl.compute_tuition())
print(student_recip.first, student_recip.last, student_recip.compute_tuition())
