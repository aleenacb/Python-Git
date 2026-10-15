#Largest Nunber in List
numbers = [12, 45, 23, 67, 34]
Largest = numbers[0]
for num in numbers:
    if num > Largest:
        Largest = num
print("Largest Number in List :", Largest)