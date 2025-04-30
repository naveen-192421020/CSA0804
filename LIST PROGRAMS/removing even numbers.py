numbers = [1, 2, 3, 4, 5, 6]
result = []
for num in numbers:
    if num % 2 != 0:
        result.append(num)
print("List after removing even numbers:", result)
