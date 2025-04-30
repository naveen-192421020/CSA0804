numbers = [3, -2, 5, -1, 6, -3]
max_sum = 0
for num in numbers:
    if num > 0:
        max_sum += num
print("Largest subsequence sum is:", max_sum)
