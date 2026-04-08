class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        return self.brand, self.model
car1 = car("Toyota","Corolla")
print(car1.display())