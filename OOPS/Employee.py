#Employee Management System
#Imagine a company has 500 employees. Every employee has: * A name, * An employee ID, * A department
#Instead of writing separate code for every employee, developers create one Employee class and use it to create different employee objects
class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department
    def display_details(self):
        print("Employee Name: ", self.name)
        print("Employee ID: ", self.emp_id)
        print("Employee Department: ", self.department)
        print("-----------------")
#Creating employee objects
emp1 = Employee("Aleena", 101, "Department")
emp2 = Employee("Priya", 102, "Testing")
emp3 = Employee("Anu", 103, "HR")

emp1.display_details()
emp2.display_details()
emp3.display_details()

#OOPS Concepts used:
# *Class:Employee
# *objects: emp1, emp2, emp3
# *Constructor: __init__()
# *Instance Variables: name, emp_id, department
# *Method: display_details

#Interview Questions
# why do we use classes and ibjects in real word applications?
# Classes and objects help organize related data and functionality into reusable units. They make applications easier to maintain, extend and manage.