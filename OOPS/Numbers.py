class Numbers:
    def __init__ (self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
n1 = Numbers(10)
n2 = Numbers(20)
print(n1 + n2)

#here n1 + n2 calls n1.__add__(n2)