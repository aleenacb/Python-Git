#Composition means creating an object inside another class
class Engine:
    def start(self):
        print("Engine Started")
class Car:
    def __init__ (self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("car is moving")
car = Car()
car.drive()