while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    rank = 'F'
    mf = m + f
    if m == -1 or f == -1:
        rank = 'F'
    elif mf >= 80:
        rank = 'A'
    elif mf >= 65 and mf < 80:
        rank = 'B'
    elif mf >= 50 and mf < 65:
        rank = 'C'
    elif mf >= 30 and mf < 50:
        if r >= 50:
            rank = 'C'
        else:
            rank = 'D'
    else:
        rank = 'F'
    print(rank)
 
