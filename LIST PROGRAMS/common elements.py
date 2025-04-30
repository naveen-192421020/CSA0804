a = [5, 6, 7]
b = [6, 7, 8]
c = []
for x in a:
    if x in b and x not in c:
        c.append(x)
print(c)
