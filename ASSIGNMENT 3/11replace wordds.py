s = "hi there hi"
old = "hi"
new = "hello"
words = s.split()
res = ""
for w in words:
    if w == old:
        res += new + " "
    else:
        res += w + " "
print(res.strip())
