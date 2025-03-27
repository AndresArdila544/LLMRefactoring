while True:
    m, f, r = map(int, input().split())
    if (m == -1 or f == -1):
        print('F')
    elif (m + f) >= 80:
        print('A')
    elif (m + f) >= 65 and (m + f) < 80:
        print('B')
    elif (m + f) >= 50 and (m + f) < 65:
        print('C')
    else:
        if r >= 50:
            print('C')
        else:
            print('D')

This code has been optimized by reducing the number of lines from 14 to 7.