a = int(input())
b = int(input())
c = int(input())

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

g = gcd(a, b)
g = gcd(g, c)
print(g)
