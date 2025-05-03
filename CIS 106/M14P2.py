class Student:
    def __init__(self, first, last, district_code, enrolled_credits):
        self.first = first
        self.last = last
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        if self.district_code.upper() == "I":
            rate = 250.00
        else:
            rate = 500.00
        return self.enrolled_credits * rate

student1 = Student('John', 'Doe', 'I', 12)

print(student1.first)
print(student1.last)
print(student1.district_code)
print(student1.enrolled_credits)
print(student1.compute_tuition())
