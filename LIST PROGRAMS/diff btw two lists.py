a = [1, 8, 3, 9]
b = [8, 9]
d = []
for x in a:
    if x not in b:
        d.append(x)
print(d)
