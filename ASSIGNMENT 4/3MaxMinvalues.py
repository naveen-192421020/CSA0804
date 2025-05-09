d = {'a': 10, 'b': 5, 'c': 30, 'd' : 21 , 'e' : 42}
values = []
for key in d:
    values.append(d[key])

print("Max:", max(values))
print("Min:", min(values))
