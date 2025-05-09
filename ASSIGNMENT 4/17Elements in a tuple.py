t = (1, 2, 3)
target = 2
found = False
for x in t:
    if x == target:
        found = True
        break
if found:
    print("Found")
else:
    print("Not Found")
