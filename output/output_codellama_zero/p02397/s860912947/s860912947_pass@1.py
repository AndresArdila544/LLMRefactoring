a, b = [], []
while True:
    x, y = map(int, input().split())
    if not (x == 0 and y == 0):
        a.append(x)
        b.append(y)
        for i in range(len(a)):
            print(min(b[i], a[i]), max(b[i], a[i]))