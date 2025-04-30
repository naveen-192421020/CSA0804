input_str = input("Enter numbers separated by space: ")
numbers = []
for part in input_str.split():
    numbers.append(int(part))
max_num = max(numbers)
min_num = min(numbers)
print("Maximum element:", max_num)
print("Minimum element:", min_num)
