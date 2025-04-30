a=int(input("Enter Size of Elemnts:"))
l=[]
for i in range(0,a):
    l.append(int(input(f"Enter Value{i+1}:")))
print("Before Removing",l)
new_list = []
for i in l:
    if i not in new_list:
        new_list.append(i)
print("After Removing",new_list)
