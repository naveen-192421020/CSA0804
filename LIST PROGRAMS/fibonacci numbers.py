n = int(input())
f = []
a = 0
b = 1
for i in range(n):
    f.append(a)
    c = a + b
    a = b
    b = c
print(f)
