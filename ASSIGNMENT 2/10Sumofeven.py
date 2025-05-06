n = int(input())
l = []
sum=0
for i in range(n):
    x = int(input())
    l.append(x)

for x in l:
    if x % 2 == 0:
        sum+=x
print(sum)
