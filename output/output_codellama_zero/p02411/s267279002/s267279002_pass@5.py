while True:
    m, f, r = map(int, input().split())
    if all([m == -1, f == -1]):
        break
    if (m + f) >= 80:
        print('A')
    elif (m + f) >= 65 and (m + f) < 80:
        print('B')
    elif (m + f) >= 50 and (m + f) < 65:
        print('C')
    elif m + f >= 30 and m + f < 50:
        if r >= 50:
            print('C')
        else:
            print('D')
    else:
        print('F')