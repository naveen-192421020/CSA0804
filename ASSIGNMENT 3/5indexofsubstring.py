s = "hello world"
sub = "world"
i = 0
found = -1
while i <= len(s) - len(sub):
    if s[i:i+len(sub)] == sub:
        found = i
        break
    i += 1
print(found)
