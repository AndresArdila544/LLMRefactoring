while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif b >= a:
        print(a, b)
    else:
        print(b, a)