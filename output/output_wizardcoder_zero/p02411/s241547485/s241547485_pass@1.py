def calculate_grade(m, f, r):
    if m == -1 or f == -1:
        return "F"
    elif 30 <= m + f < 50:
        return "D"
    elif (50 <= m + f < 65) and r >= 50:
        return "C"
    elif 50 <= m + f < 80:
        return "B"
    else:
        return "A"

while True:
    m,f,r = map(int, input().split())
    if m == f == r == -1:
        break
    print(calculate_grade(m, f, r))