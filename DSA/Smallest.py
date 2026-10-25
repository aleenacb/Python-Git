numbers = [18, 7, 24, 3, 12]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest", smallest)