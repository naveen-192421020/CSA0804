s = "babad"
n = len(s)
longest = ""
for i in range(n):
    for j in range(i, n):
        part = s[i:j+1]
        if part == part[::-1]:
            if len(part) > len(longest):
                longest = part
print(longest)
