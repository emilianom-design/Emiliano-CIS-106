class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def bonus(self, rate):
        return float(rate) * float(self.pay)

class Manager(Employee):
    def long_term_bonus(self):
        return 0.40 * self.pay

emp1 = Employee('john', 'smith', 50000.00)
emp2 = Employee('bill', 'williams', 55000.00)

mgr1 = Manager('alice', 'johnson', 80000.00)
mgr2 = Manager('bob', 'williams', 90000.00)

print(emp1.email)
print(emp1.first)
print(emp1.last)
print(emp1.pay)
print(emp1.bonus(0.10))

print(emp2.email)
print(emp2.first)
print(emp2.last)
print(emp2.pay)
print(emp2.bonus(0.15))

print(mgr1.email)
print(mgr1.first)
print(mgr1.last)
print(mgr1.pay)
print(mgr1.long_term_bonus())

print(mgr2.email)
print(mgr2.first)
print(mgr2.last)
print(mgr2.pay)
print(mgr2.long_term_bonus())
