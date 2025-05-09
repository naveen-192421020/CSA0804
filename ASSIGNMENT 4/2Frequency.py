d = {'a': 2, 'b': 3, 'c': 2}
freq = {}
for key in d:
    value = d[key]
    if value in freq:
        freq[value] += 1
    else:
        freq[value] = 1
print(freq)
