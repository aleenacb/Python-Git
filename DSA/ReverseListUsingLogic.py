numbers = [1, 2, 3, 4, 5]
left = 0#points to first element
right = len(numbers) - 1#points to last element
while left < right:#continues until the pointers
    numbers[left],numbers[right] = numbers[right],numbers[left]#swaps the two numbers
    left += 1#moves left forward
    right -= 1#moves right backward
print(numbers)