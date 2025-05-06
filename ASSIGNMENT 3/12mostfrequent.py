s = input("Enter")
words = s.split()
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
mx = 0
ans = ""
for w in freq:
    if freq[w] > mx:
        mx = freq[w]
        ans = w
print(ans)
