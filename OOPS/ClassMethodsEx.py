class Employee:
    company = "Google"
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
Employee.change_company("Microsoft")
print(Employee.company)