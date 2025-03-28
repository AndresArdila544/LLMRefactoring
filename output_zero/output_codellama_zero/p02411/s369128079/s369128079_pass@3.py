while True:
    m, f, r = map(int, raw_input().split())
    if m == -1 and f == -1 and r == -1: break
    s = m + f
    g = (2 if r >= 50 else 3) if s < 30 else ((2 if s >= 65 else 1) if s < 50 else 0) if m == -1 or f == -1 else 5)