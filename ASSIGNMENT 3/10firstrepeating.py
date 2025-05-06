s = "abcab"
seen = ""
for c in s:
    if c in seen:
        print(c)
        break
    seen += c
