import sys
while True:
    n = input()
    if n == '0 0': break
    x, y = map(int, n.split())
    print((x > y) * (y, x) + (x <= y) * n)