d = {'x': 100, 'y': 200}
value = 100
found = False
for v in d:
    if d[v] == value:
        found = True
        break
if(found):
    print("Found")
else:
    print("Not Found")
