#Global vs Local With same name
a = 1
def f():
    print("f():", a)
def g():
    a = 2
    print("g():", a)
def h():
    global a
    a = 3
    print("h():",a)
print("Global",a)
f()
print("Global",a)
g()
print("Global",a)
h()
print("Global",a)