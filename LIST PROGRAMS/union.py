a = [1, 2, 3]
b = [3, 4, 5]
u = []
for x in a:
    u.append(x)
for x in b:
    if x not in u:
        u.append(x)
print(u)
