arr= [4, 5, 1, 2, 1, 4, 5, 3]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for num in arr:
    if freq[num] == 1:
        print("First Non Repeating Element:", num)
        break