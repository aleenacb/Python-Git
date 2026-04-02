#Pass by reference and pass by value
def myFun(x):
    x[0] = 20
lst = [10, 11, 12, 13]
myFun(lst)
print(lst)

def myFun2(x):
    x = 20
a = 10
myFun2(a)
print(a)
