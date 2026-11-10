class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price
  def display(self):
    print(self.name, self.price)
p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 20000)
p1.display()
p2.display()
