d = {'x': 1, 'y': 2}
key_to_remove = 'x'
new_d = {}
for k in d:
    if k != key_to_remove:
        new_d[k] = d[k]
print(new_d)
