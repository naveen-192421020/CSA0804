s = "aabbbcccc"
freq = {}
for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
vals = sorted(freq.values(), reverse=True)
sec = vals[1]
for k in freq:
    if freq[k] == sec:
        print(k)
        break
