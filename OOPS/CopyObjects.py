import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
#Shallow copy: creates a new outer object but shares nested objects
#Deep copy: Creates a new outer object and copies nested objects too