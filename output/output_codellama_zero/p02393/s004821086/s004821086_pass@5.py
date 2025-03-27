a, b, c = map(int, input().split())
if a > b:
    tmp = a
    a = b
    b = tmp
if b > c:
    tmp = b
    b = c
    c = tmp
print(a, b, c)