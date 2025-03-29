while True:
    m, f, r = list(map(int, input().split()))
    if (m == -1 or f == -1) and (r > 50):
        print("F")
    elif (m + f < 30) and (r <= 50):
        print("D")
    elif (m + f >= 30) and (m + f < 65) and (r >= 50):
        print("C")
    elif (m + f >= 65) and (m + f < 80) and (r >= 50):
        print("B")
    else:
        print("A")