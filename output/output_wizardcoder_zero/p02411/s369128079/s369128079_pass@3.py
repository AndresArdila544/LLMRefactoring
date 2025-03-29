while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1: break
    else:
        s = m + f
        g = 5 if (m == -1 or f == -1) or s < 30 else (2 if 30 <= s < 50 and r >= 50 else 3 if 50 <= s < 65 else 1 if 65 <= s < 80 else 0)
        print('ABCDEF'[g])