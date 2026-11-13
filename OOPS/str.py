class Student:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def __str__ (self):
        return f"Name: {self.name}, Age: {self.age}"
s1 = Student("Aleena",22)
print(s1)

# __str__ should return string