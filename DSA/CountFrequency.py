arr = [1, 2, 3, 2, 1, 4, 2]
# create an empty dictionary
freq = {}
#Traverse each element in the list
for num in arr:
    #Check wther the element already exists
    if num in freq:
        #If element already exists then increase frequency count by 1
        freq[num] += 1
    else:
        #Otherwise initialize its count by 1
        freq[num] = 1

#freq.items - it gets both key and value from a dictionary and traverses key and values
for key, value in freq.items():
    print(key, "appears", value, "times")