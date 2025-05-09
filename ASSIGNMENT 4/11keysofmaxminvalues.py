d = {'a': 3, 'b': 1, 'c': 2}
keys = list(d)
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        if d[keys[i]] > d[keys[j]]:
            keys[i], keys[j] = keys[j], keys[i]

sorted_d = {}
for k in keys:
    sorted_d[k] = d[k]
print(sorted_d)
