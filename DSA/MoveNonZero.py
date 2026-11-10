arr= [0, 1, 0, 3, 12]
zero = []
non_zero = []
for num in arr:
    if num != 0:
        non_zero.append(num)
    else:
        zero.append(num)
result = non_zero + zero
print("Sorted Array:", result)