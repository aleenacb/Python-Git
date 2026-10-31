arr = [1, 2, 2, 3, 3, 3, 4, 4]
freq = {}
SecHighest = 0
Highest = 0
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print("Second Highest Frequency:", end = " ")
for count in freq.values():
    if count > Highest:
        SecHighest = Highest
        Highest = count
    elif count < Highest and count > SecHighest:
        SecHighest = count
print(count)
