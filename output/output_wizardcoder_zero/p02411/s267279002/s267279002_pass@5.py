def calculate_grade(marks, final):
    if marks == -1 or final == -1:
        return 'F'
    elif (marks + final) >= 80:
        return 'A'
    elif (marks + final) >= 65 and (marks + final) < 80:
        return 'B'
    elif (marks + final) >= 50 and (marks + final) < 65:
        if r >= 50:
            return 'C'
        else:
            return 'D'
    else:
        return 'F'

while True:
    m, f = map(int, input().split())
    if m == -1 or f == -1:
        break
    r = int(input())
    print(calculate_grade(m, f))