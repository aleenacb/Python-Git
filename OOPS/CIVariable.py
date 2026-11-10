#Class Variable and Instance Variable
class Employee:
    company = "Google" # class Variable
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
e1 = Employee("Aleena", 30000)
e2 = Employee("Rahul", 70000)
print(e1.company)
print(e1.name)

print(e2.company)
print(e2.name)