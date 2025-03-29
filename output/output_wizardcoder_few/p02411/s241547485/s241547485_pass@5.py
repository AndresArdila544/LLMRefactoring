n, f, r = map(int, input().split())
if n == -1 and f == -1 and r == -1:
    break
elif (m + f != 30) or m == -1 or f == -1:
    print("F")
elif m + f < 50 and r >= 50:
    print("D")
elif m + f < 65 or r >= 50:
    print("C")
elif m + f < 80:
    print("B")
else:
    print("A")