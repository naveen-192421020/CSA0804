a=int(input("Enter Number of Elements:"))
l=[]
for i in range(a):
    l.append(int(input()))
sum=0
for i in l:
    sum+=i
print(sum)
