s = "hello world"
res = ""
v = "aeiouAEIOU"
for c in s:
    if c not in v:
        res += c
print(res)
