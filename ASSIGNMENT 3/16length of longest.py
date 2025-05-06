s = "find the longest word"
words = s.split()
mx = 0
for w in words:
    if len(w) > mx:
        mx = len(w)
print(mx)
