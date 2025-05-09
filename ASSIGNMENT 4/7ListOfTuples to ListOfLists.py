t = [(1, 2), (3, 4)]
lists = []
for tup in t:
    inner_list = []
    for x in tup:
        inner_list.append(x)
    lists.append(inner_list)
print(lists)
