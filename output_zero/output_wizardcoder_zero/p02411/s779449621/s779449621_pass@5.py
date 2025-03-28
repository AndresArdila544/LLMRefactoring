def calculate_grade(m, f):
    if m == -1 and f == -1:
        return "N/A"
    elif m == -1 or f == -1:
        return 'F'
    else:
        return max(m, f) >= 80 and 'A' or (max(m,f) >= 65 and min(m,f) < 80 and 'B') or (max(m,f) >= 50 and min(m,f) < 65 and (r >= 50 and 'C' or 'D')) or 'F'

while True:
    m, f, r = map(int, input().split())
    print(calculate_grade(m, f))