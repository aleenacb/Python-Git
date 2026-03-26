d = {1:"Geeks", "name":"for",3:"geeks"}
print(d["name"])
print(d.get(3))

x = {1, 2, 3}
print(type(x))

a = {'a':1, 'b':2}
b = a
a = {'c',3}
print(b)

x = 1
y = 1
z = x + y
print(id(x), id(z))