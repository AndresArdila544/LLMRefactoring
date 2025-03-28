```
while True:
    m,f,r = map(int, raw_input().split())
    if (m == -1 and f == -1 and r == -1): break
    elif (m == -1 or f == -1) or s < 30: g=5
    else: g = {
        30 <= s and s < 50: 2 if r >= 50 else 3,
        50 <= s and s < 65: 2,
        65 <= s and s < 80: 1,
        True: 0 }[True]
    print 'ABCDEF'[g]
```