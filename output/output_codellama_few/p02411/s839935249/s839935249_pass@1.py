result = []
while True:
    m, f, r = (int(x) for x in input().split())
    if m == -1 and f == -1 and r == -1:
        break
    if m < 0 or f < 0:
        result.append("F")
    elif m + f >= 80:
        result.append("A")
    elif m + f >= 65:
        result.append("B")
    elif m + f >= 50:
        result.append("C")
    elif m + f >= 30 and r >= 50:
        result.append("C")
    else:
        result.append("D")
for grade in result:
    print(grade)