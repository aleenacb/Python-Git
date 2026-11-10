arr = [1, 3, 5, 2, 2]
leftSum = 0
totalSum = sum(arr)
for i, num in enumerate(arr):
    rightSum = totalSum - leftSum - num
    if leftSum == rightSum:
        print("Equilibrium Index:",i, end = " ")
    leftSum += num
