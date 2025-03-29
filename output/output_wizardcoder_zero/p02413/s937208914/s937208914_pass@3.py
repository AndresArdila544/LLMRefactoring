a = []
gyou = [0] * len(range(len(a[0]) if a else 1)
retu = []
s = sum(map(sum, a))

for row in a:
    gyou = sum(row)
    retu.append(row)
    print(" ".join(map(str, row), sum(row))
if len(a) > 1:
    print(" ".join(map(str, gyou)), s)