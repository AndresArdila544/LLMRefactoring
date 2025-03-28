while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    rank = 'F'
    mf = m + f
    if m != -1 and f != -1 and mf >= 80:
        rank = 'A'
    elif m != -1 and f != -1 and mf >= 65 and mf < 80:
        rank = 'B'
    elif m != -1 and f != -1 and mf >= 50 and mf < 65:
        rank = 'C'
    elif m != -1 and f != -1 and mf >= 30 and mf < 50:
        if r >= 50:
            rank = 'C'
        else:
            rank = 'D'
    print(rank)