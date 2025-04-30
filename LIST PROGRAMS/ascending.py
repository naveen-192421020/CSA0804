input_str = input("Enter numbers separated by space: ")
numbers = input_str.split()
numbers = [int(num) for num in numbers]
numbers.sort()
print(numbers)
