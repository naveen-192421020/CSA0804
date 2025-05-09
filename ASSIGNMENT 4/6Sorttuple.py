t = (3, 1, 4, 2)
lst = []
for x in t:
    lst.append(x)
lst.sort()
t=tuple()
for x in lst:
    t += (x,)
print(t)
