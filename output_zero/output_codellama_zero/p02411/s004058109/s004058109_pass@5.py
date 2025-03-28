while True:
    (m, f, r) = [int(i) for i in input().split() if i != -1]
    s = m + f

    if not s >= 30 or r < 50:
        print('F')
    elif s >= 50 and r < 50:
        print('D')
    elif s >= 65 and r < 50:
        print('C')
    elif s >= 80 and r < 50:
        print('B')
    else:
        print('A')