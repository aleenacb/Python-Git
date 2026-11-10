items = [2, 4, 6, 8, 10]
target = 14
def linearSearch(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return 1