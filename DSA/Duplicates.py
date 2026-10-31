arr = [1, 2, 3, 2, 1, 4, 2]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print("Duplicates:", end=" ")
for key, value in freq.items():
    if value > 1:
        print(key, end=" ")