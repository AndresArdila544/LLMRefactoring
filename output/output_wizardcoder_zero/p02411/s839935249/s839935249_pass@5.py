result = []
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1:
        break
    result.append("F" if m < 0 or f < 0 else "A" if m + f >= 80 else "B" if m + f >= 65 else "C" if m + f >= 50 and r >= 50 else "D" if m + f >= 30 else "F")
for grade in result:
    print(grade)