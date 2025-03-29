import sys
n, x = (int(s) for s in sys.stdin.readline().split())
if n == 0 and x == 0:
    break
cnt = 0
for a in range(1, n):
    if a >= x:
        break
    for b in range(a+1, n):
        ab = a + b
        if ab >= x:
            break
        for c in range(b+1, n):
            abc = ab + c
            if abc == x:
                cnt += 1
                break
print(cnt)