def next_greater(nums):
    n = len(nums)
    res = [-1] * n
    stack = []
    
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            res[stack.pop()] = nums[i % n]
        
        if i < n:
            stack.append(i)
    
    return res

print(next_greater([1,2,1]))
