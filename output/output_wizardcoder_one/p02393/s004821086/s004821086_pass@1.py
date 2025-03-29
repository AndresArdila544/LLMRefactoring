a, b, c = map(int, input().split())
if a > b:
    tmp = a
    a = b
    b = tmp
if b > c:
    if a > b:
        a, b = b, a
print(a, b, c)