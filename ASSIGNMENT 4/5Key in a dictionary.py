d = {'x': 100, 'y': 200}
key = 'x'
found = False
for k in d:
    if k == key:
        found = True
        break
if found:
    print("Found")
else:
    print("Not Found")
