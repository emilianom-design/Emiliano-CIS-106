class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b

emp11 = Employee('frank', 'alvino', 60000.00)

print(emp11.email)
print(emp11.first)
print(emp11.last)
print(emp11.pay)
print(emp11.bonus(0.10))
print(emp11.bonus(0.20))
