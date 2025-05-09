d = {'a': 1, 'b': 2}
result = tuple()
for key in d:
    result+=(d[key],)
print(result)
