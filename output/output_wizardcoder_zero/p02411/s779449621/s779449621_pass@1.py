def calculate_gpa(m, f):
    if m == -1 and f == -1:
        return 'N/A'  # This means no inputs were given.
    elif m >= 80 or f >= 80:
        return 'A'
    elif (m + f) / 2 >= 75:
        return 'A-'
    elif (m + f) / 2 >= 65:
        return 'B+' if m > f else ('C+', '')[f > m]  # This line returns C+ for m > f and B+ otherwise.
    elif (m + f) / 2 >= 60:
        return 'B'
    elif (m + f) / 2 >= 50:
        if r >= 50:
            return 'C'
        else:
            return 'D'
    else:
        return 'F'
        
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    print(calculate_gpa(m, f))