s = input()
if "@" in s:
    if s[-4:] == ".com" or s[-3:] == ".in" or s[-4:] == ".org":
        print("Yes")
    else:
        print("No")
else:
    print("No")
