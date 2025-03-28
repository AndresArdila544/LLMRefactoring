import sys
while True:
    n, x = map(int, input().split())
    if not (n and x): break
    cnt = sum(a + b > x for a in range(1, n) for b in range(a+1, n))
    print(cnt)