class Student:
    def __init__ (self, name):
        self.name = name
    def __str__ (self):
        return self.name
s1 = Student("Aleena")
print(s1)