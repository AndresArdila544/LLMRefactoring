Here is the refactored code:

a, b, c = map(int, input().split())

if a > b and b > c:
    print(c, b, a)
elif a > b and a > c:
    print(b, c, a)
elif b > a and b > c:
    print(c, a, b)
elif b > a and a > c:
    print(a, b, c)
else:
    print(a, b, c)