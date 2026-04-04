s = "Python is great"
def fun():
    global s
    s += "GFG"
    s = "Look for GeeksforGeeks Python section"
    print(s)
fun()
print(s)

x  = 10
def myfun():
    x = 5
    print(x)
myfun()

x = 10
def mf():
    global x
    x = 20
    print(x)
mf()
print(x)