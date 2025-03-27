while True:
    m, f, r = map(int, input().split())
    if -1 not in (m, f, r):
        x = max(0, m) + max(0, f)
        grade = 'F' if x < 30 else 'A' if 80 <= x else 'B' if 65 <= x else 'C' if 50 <= x else 'D'