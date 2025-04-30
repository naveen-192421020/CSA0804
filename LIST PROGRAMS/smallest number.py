a=int(input("Enter Number of Elements:"))
l=[]
for i in range(a):
    l.append(int(input()))
s=l[0]
for i in l:
    if i<=s:
        s=i
print("Smallest is",s)
