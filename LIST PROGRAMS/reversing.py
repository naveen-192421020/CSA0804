size = int(input("Enter number of elements: "))
numbers = []

for i in range(size):
    num = int(input("Enter element {}: ".format(i + 1)))
    numbers.append(num)

reversed_list = numbers[::-1]
print("Reversed list:", reversed_list
