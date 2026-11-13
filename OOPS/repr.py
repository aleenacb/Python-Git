class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f"Product('{self.name}',{self.price})"
p1 = Product("Laptop", 50000)
print(repr(p1))
print(str(p1))