t = (1, 2, 3)
rev = ()
for i in range(len(t) - 1, -1, -1):
    rev += (t[i],)
print(rev)
