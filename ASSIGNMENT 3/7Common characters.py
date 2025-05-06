a = input("Enter 1")
b = input("Enter 2")
res = ""
for c in a:
    if c in b and c not in res:
        res += c
print(res)
