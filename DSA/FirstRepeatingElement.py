numbers = [4, 2, 7, 2, 5, 4, 8]
seen = set()
freq= {}
for nums in numbers:
    if nums in freq:
        freq[nums] += 1
    else:
        freq[nums] = 1

for nums in numbers:
    if nums in seen:
        print("First Repeating element", nums)    
        break
    else:
        seen.add(nums)   

