arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum
print("Maximum of 3 elements:", end=" ")
for i in range(k, len(arr)):
    window_sum += arr[i]
    window_sum -= arr[i - k]

    max_sum = max(max_sum, window_sum)
print(max_sum)