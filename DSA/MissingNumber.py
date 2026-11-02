numbers = [1, 2, 4, 5, 6]
n = len(numbers) + 1
total = n * (n + 1)//2
actual_Sum = sum(numbers)
missing = total - actual_Sum
print("Missing Number", missing)
