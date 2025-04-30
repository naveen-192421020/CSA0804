numbers = [1, 2, 3, 4, 5]
element = int(input("Enter the element to find its index: "))

if element in numbers:
    index = numbers.index(element)
    print("Index of", element, "is:", index)
else:
    print("Element not found in the list.")
