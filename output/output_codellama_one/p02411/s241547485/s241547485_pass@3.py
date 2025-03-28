import math
x1, y1, x2, y2 = map(float, input().split())
d = math.hypot(x1-x2, y1-y2)
print(d)
while True:
    m, f, r = list(map(int, input().split()))
    if m == -1 or f == -1 or m + f < 30:
        print("F")
    elif m + f >= 50 and r < 50:
        print("D")
    elif m + f >= 65 or r >= 50:
        print("C")
    elif m + f >= 80:
        print("B")
    else:
        print("A")