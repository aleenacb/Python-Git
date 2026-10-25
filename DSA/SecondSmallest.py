numbers = [10, 25, 8, 40, 15]
smallest = float('inf')
sec_smallest = float('inf')

for num in numbers:
    if num < smallest:
        sec_smallest = smallest
        smallest = num
    elif num < sec_smallest and num != smallest:
        sec_smallest = num
print(sec_smallest)
