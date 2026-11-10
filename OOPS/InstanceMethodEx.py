class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name:",self.name)
        print("salary:", self.marks)

s1 = Student("Aleena", 90)
s1.display()