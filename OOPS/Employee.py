class Employee:
    company = "TCS"
    def __init__(self, name):
        self.name = name
e1 = Employee("Anu")
e2 = Employee("Ravi")
e1.company = "Infosys"
print(e1.company)
print(e2.company)