arr = [2, 2, 1, 2, 3, 2, 2]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print("Majority Threshold:", end = " ")
for key in freq:
    if freq[key] > len(arr)//2:
        print(key, end = " ")


