s = input("ENter:")
found = False
for c in s:
    if c.isdigit():
        found = True
        break
if found:
    print("Yes")
else:
    print("No")
