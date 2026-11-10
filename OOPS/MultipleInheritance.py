#Multiple Inheritance: means one child inherits properties and methods from more than one parent class
class Father:
    def gardening(self):
        print("Father know gardenning")
class Mother:
    def painting(self):
        print("Mother knows painting")
class Child(Father, Mother):
    def coding(self):
        print("Child knows coding")
obj = Child()
obj.gardening()
obj.painting()
obj.coding()