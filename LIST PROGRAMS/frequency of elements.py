a = [2, 4, 8, 5, 1, 3, 6, 7, 2, 4, 4]
c= []

for i in range(len(a)):
    if a[i] not in c:
        times = 0
        for j in range(len(a)):
            if a[i] == a[j]:
                times += 1
        print(f"{a[i]} occurs {times} times")
        c.append(a[i])
