while True:
    m, f, r = map(int, input().split())
    x = max(0, m) + max(0, f)
    if x == 0 and (m==-1 or f==-1):
        break
     elif 80 <= x:
            grade = 'A'
        elif 65 <= x and x < 80:
            grade = 'B'
        elif 50 <= x and x < 65:
            grade = 'C'
        elif 30 <= x and x < 50:
            if 50 <= r:
                grade = 'C'
            else:
                grade = 'D'
        else:
            grade = 'F'
        print(grade)