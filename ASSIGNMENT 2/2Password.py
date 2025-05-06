s = input()
upper = False
lower = False
digit = False

if len(s) >= 8:
    for c in s:
        if c.isupper():
            upper = True
        if c.islower():
            lower = True
        if c.isdigit():
            digit = True

if upper and lower and digit:
    print("Valid")
else:
    print("Invalid")
