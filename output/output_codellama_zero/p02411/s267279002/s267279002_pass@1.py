while True:
    m, f, r = map(int, input().split())
    if (m == -1) and (f == -1):
        break
    elif (m + f) >= 80:
        print('A')
    elif (m + f) >= 65 and (m + f) < 80:
        print('B')
    elif (m + f) >= 50 and (m + f) < 65:
        print('C')
    elif ((m + f) >= 30) and (r >= 50):
        print('C')
    else:
        print('F')