t = (10, 20, 30)
target = 20
index = 0
for i in range(len(t)):
    if t[i] == target:
        index = i
        break
print(index)
