class Person:
    def introduce(self):
        print("Iam a person")
class Student(Person):
    pass
s1 = Student()
s1.introduce()