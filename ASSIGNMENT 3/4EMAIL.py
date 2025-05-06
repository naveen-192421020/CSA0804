s = "abc@example.com"
if "@" in s and s[-4:] == ".com":
    print("Valid")
else:
    print("Invalid")
