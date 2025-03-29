a, b, c = map(int, input().split())
if a > b and a > c:
    print(c, b, a)
elif a > b and a < c:
    print(b, a, c)