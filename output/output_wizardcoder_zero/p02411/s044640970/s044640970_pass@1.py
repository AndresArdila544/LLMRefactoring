while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    elif m == -1 or f == -1:
        print("F")
    else:
        if m + f >= 80:
            print("A")
        elif m + f >= 65:
            print("B")
        elif m + f >= 50 and r >= 50:
            print("C")
        else:
            print("D")
        elif m + f < 50:
            print("F")