import math

while True:
    m, f, r = list(map(int, input().split()))
    if m == -1 and f == -1:
        break
    elif m + f < 30 or (m + f < 50 and r < 50):
        print("F")
    elif m + f < 65 or r >= 50:
        print("D")
    elif m + f < 80:
        print("B")
    else:
        print("A")