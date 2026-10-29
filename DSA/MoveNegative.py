numbers = [3, -1, 4, -5, 2, -8, 6]
negative = []
non_negative = []
for num in numbers:
    if num < 0:
        negative.append(num)
    else:
        non_negative.append(num)
result = negative + non_negative
print(result)