size = int(input("Enter number of elements: "))
numbers = []

for i in range(size):
    num = int(input("Enter an element: "))
    numbers.append(num)

if size < 2:
    print("Second largest number not found.")
else:
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    second = None
    for num in numbers:
        if num != largest:
            if second is None or num > second:
                second = num

    if second is None:
        print("All elements are equal. No second largest number.")
    else:
        print("Second largest number is:", second)
